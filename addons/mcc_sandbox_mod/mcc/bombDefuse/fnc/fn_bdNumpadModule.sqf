/*=================================================================MCC_fnc_bdCreateManual==================================================================================
  start a bomb defuse numpad module
  IN <>
    _difficulty - STRING
    _ctrlGroup - CTRL
    _serialNumber - INTEGER
*/

private ["_difficulty","_ctrlGroup","_display","_idc","_buttons","_buttonsCombinations","_ratio","_ctrl","_posX","_posY","_ctrls","_serialNumber","_answers","_symbol","_index","_showSymbols"];
disableSerialization;
_difficulty = _this select 0;
_ctrlGroup = _this select 1;
_serialNumber = _this select 2;

_display = ctrlParent _ctrlGroup;
_idc = ctrlIDC _ctrlGroup *1000;

_buttons = switch (toLower _difficulty) do {
  case "hard": {12};
  case "medium": {9};
  default {6};
};

if ((_serialNumber mod 7) == 0) then {
    _buttonsCombinations = ["^","p","2","P","M","N","0","n","o","%","#",")","}","|","i","m","I"];
} else {
     _buttonsCombinations = ["0","m",")","o","|","#","^","n","P","i","N","2","I","M","%","p","}"];
};

_ratio =safezoneW / safezoneH;
_ctrls = [];
_answers = [];
_showSymbols = [];

_posX = 0.025;
_posY = 0.025;

//Make the buttons
for "_i" from 1 to _buttons do {
    _symbol = _buttonsCombinations call bis_fnc_selectRandom;
    while {_symbol in _showSymbols} do {
        _symbol = _buttonsCombinations call bis_fnc_selectRandom;
    };
    _showSymbols pushBack _symbol;
    _answers pushBack (_buttonsCombinations find _symbol);

    //Create Symbol
    _ctrl = _display ctrlCreate ["RscButton", _idc+_i,_ctrlGroup];
    _ctrl ctrlSetText _symbol;
    _ctrl ctrlSetTextColor [0,0.8,0,0.8];
    _ctrl ctrlSetBackgroundColor [0,0,0,0.8];
    _ctrl ctrlSetPosition [_posX*_ratio, _posY *_ratio, 0.04*_ratio, 0.04*_ratio];
    _ctrl ctrlCommit 0;

    _ctrls pushBack _idc+_i;

    //move left a box max 4 box in a row
    if (count _ctrls mod 3 != 0) then {
        _posX = _posX + (0.04*_ratio)*1.1;
    } else {
        //if not last variable in the array move down a line
        if (_i != _buttons) then {
            _posY = _posY + (0.04*_ratio)*1.1;
            _posX = 0.025;
        };
    };
};

//Find the correct order and sort the answers
_answers sort true;
for "_i" from 0 to (count _answers)-1 do {
    _answers set [_i, _buttonsCombinations select (_answers select _i)];
};

//Add EH
{
    _ctrl = _display displayctrl _x;
_ctrl ctrlAddEventHandler ['MouseButtonUp',format ["_ctrl = _this select 0;\n_display = ctrlParent _ctrl;\n_index = 0;\n_answers = %2;\n{\n    if !(ctrlEnabled (_display displayctrl _x)) then {_index = _index+1};\n} forEach %1;\n\nif (ctrlText _ctrl == _answers select _index) then {\n    _ctrl ctrlEnable false;\n     playsound 'RscDisplayCurator_ping02';\n    if (count _answers -1 == _index) then {\n        (_display displayctrl %3) ctrlshow false;\n    };\n} else {\n    player setVariable ['MCC_bombDefuseStrikes',(player getVariable ['MCC_bombDefuseStrikes',0])+1];\n    playsound 'AlarmCar';\n};",_ctrls,_answers,ctrlIDC _ctrlGroup]];
} forEach _ctrls;

//==================================================================MCC_fnc_broadcastWoosh======================================================================================
// Play MCC_woosh (optional) and show a short dynamic text. Message is treated as plain text.
//==============================================================================================================================================================================
params [
	["_msg", "", [""]],
	["_playWoosh", true, [true]]
];

if (_msg == "") exitWith {};

private _clean = "";
private _skip = false;
{
	if (_x == "<") then {
		_skip = true;
	} else {
		if (_x == ">") then {
			_skip = false;
		} else {
			if (!_skip) then {
				_clean = _clean + _x;
			};
		};
	};
} forEach (_msg splitString "");

if (_clean == "") exitWith {};

if (_playWoosh) then {
	playSound "MCC_woosh";
};

private _html = format ["<t size='1' font='puristaLight' color='#FFFFFF'>%1</t>", _clean];
[_html, 0, 0.2, 5, 1, 0.0] spawn BIS_fnc_dynamicText;

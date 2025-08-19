private ["_message","_messageFinal","_time","_ok","_type","_nul","_stance"];
// By: Shay_gman
// Version: 1.1 (May 2012)
#define MCC_playerConsoleLoading_IDD 2991

#define MCC_ConsoleLoadingText 9105
disableSerialization;

_type = (_this select 3) select 0; 								//Switch we are opening the console or the other options

closedialog 0;
_ok = createDialog "MCC_playerConsoleLoading";

_time = time + 3;

if (_type == 0) then {\t\t\t\t\t\t\t\t\t\t//Opening the console
\tif (vehicle player == player ) then
\t\t{
\t\t\tswitch (stance player) do
\t\t\t\t{
\t\t\t\t   case "STAND":
\t\t\t\t\t{
\t\t\t\t\t\t_stance = "AinvPercMstpSrasWrflDnon";
\t\t\t\t\t};

\t\t\t\t\tcase "CROUCH":
\t\t\t\t\t{
\t\t\t\t\t\t_stance = "AinvPknlMstpSrasWrflDnon";
\t\t\t\t\t};

\t\t\t\t\tcase "LYING":
\t\t\t\t\t{
\t\t\t\t\t\t_stance = "AinvPpneMstpSrasWrflDnon";
\t\t\t\t\t};

\t\t\t\t\tdefault
\t\t\t\t\t{
\t\t\t\t\t\t_stance = "";
\t\t\t\t\t}
\t\t\t\t};
\t\t\tplayer playMove _stance;
\t\t};
\tif (MCC_CASConsoleFirstTime) then
\t{
\t\twhile {_time > time && dialog} do
\t\t{
\t\t\t_message = "";
\t\t\t_messageFinal = ["S","e","a","r","c","h","i","n","g"," ","S","a","t","e","l","l","i","t","e","s",".",".",".",".","."];
\t\t\tfor "_i" from 0 to (count _messageFinal - 1) do {
\t\t\t\t_message = _message + (_messageFinal select _i);
\t\t\t\tctrlSetText [9105, _message];
\t\t\t\tsleep 0.05;
\t\t\t};
\t\t};
\t\tMCC_CASConsoleFirstTime = false;
\t};

\tif (dialog) then
\t{
\t\t_time = time + random 1;
\t\twhile {_time > time && dialog} do
\t\t{
\t\t\t_message = "";
\t\t\t_messageFinal = ["C","o","n","n","e","c","t","i","n","g",".",".",".",".","."];
\t\t\tfor "_i" from 0 to (count _messageFinal - 1) do
\t\t\t{
\t\t\t\t_message = _message + (_messageFinal select _i);
\t\t\t\tctrlSetText [9105, _message];
\t\t\t\tsleep 0.05;
\t\t\t};
\t\t};
\t};

\t_commander = ((MCC_server getVariable [format ["CP_commander%1",side player],""]) == getPlayerUID player) or ("MCC_itemConsole" in (assignedItems player));

\t//sign in
\tif (dialog && _commander) then
\t{
\t\tclosedialog 0;
\t\t_ok = createDialog "MCC_playerConsole";
\t};

\t//access denied
\tif (dialog && !_commander) then
\t{
\t\tctrlSetText [9105, "Access denied: Not commander"];
\t\tsleep 2;
\t\tclosedialog 0;
\t};
};

if (_type == 1) then {\t\t\t\t\t\t\t\t\t\t//Switching to Artillery
\t_time = time + random 2;
\twhile {_time > time && dialog} do {
\t\t_message = "";
\t\t_messageFinal = ["C","o","n","n","e","c","t","i","n","g"," ","S","t","e","e","l"," ","R","a","i","n",".",".","."];
\t\tfor "_i" from 0 to (count _messageFinal - 1) do {
\t\t\t_message = _message + (_messageFinal select _i);
\t\t\tctrlSetText [9105, _message];
\t\t\tsleep 0.05;
\t\t};
\t};
\tif (dialog) then {
\t\tclosedialog 0;
\t\tMCC_Console1Open = false;
\t\tMCC_Console2Open = false;
\t\tMCC_Console3Open = false;
\t\tMCC_Console4Open = true;
\t\t_nul=[1] execVM MCC_path + "bon_artillery\dialog\openMenu.sqf";
\t};
};



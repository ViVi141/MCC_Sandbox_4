/*==================================================================MCC_fnc_RSTakeCommander===============================================================================
// Call from a button only Become a commander
==============================================================================================================================================================================*/
private ["_commander"];

_commander = MCC_server getVariable [format ["CP_commander%1",side player],""];

//Become a commander
if (_commander == "") then {
    [format ["%1 logged in as the commander", name player]] remoteExec ["MCC_fnc_broadcastWoosh", 0, false];
    MCC_server setVariable [format ["CP_commander%1",(player getVariable ["CP_side",  playerside])],getPlayerUID player, true];

    //Handle radio channel side
    [player, true, (missionNamespace getVariable ["MCC_radioChannel_1",1])] remoteExec ["MCC_fnc_assignChannelServer", 2, false];
} else {
    //Leave commander
    if (_commander == getPlayerUID player) then {
        [format ["%1 is no longer the commander", name player]] remoteExec ["MCC_fnc_broadcastWoosh", 0, false];
        MCC_server setVariable [format ["CP_commander%1",(player getVariable ["CP_side",  playerside])],"", true];

        //Handle radio channel side
        [player, false, (missionNamespace getVariable ["MCC_radioChannel_1",1])] remoteExec ["MCC_fnc_assignChannelServer", 2, false];
    } else  {
        private ["_lastMutiny","_numberPlayers","_previousCommander"];
        //Start Mutiny
        _lastMutiny = MCC_server getVariable [format ["CP_commander%1_lastMutiny",(player getVariable ["CP_side",  playerside])],time];

        if (_lastMutiny <= time) then {
            _previousCommander = objectFromNetId (MCC_server getVariable [format ["CP_commander%1",(player getVariable ["CP_side",  playerside])],""]);

            MCC_server setVariable [format ["CP_commander%1_lastMutiny",(player getVariable ["CP_side",  playerside])],(time + 300), true];
            CP_mutiny = 0;
            publicVariable "CP_mutiny";
            sleep 1;
            [format ["%1 have started a mutiny. do you want to kick the commander - %2?", name player, _previousCommander], "MUTINY" , "CP_mutiny"] remoteExec ["MCC_fnc_vote", (player getVariable ["CP_side",  playerside]), false];
            sleep 30;
            _numberPlayers = (player getVariable ["CP_side",  playerside]) countSide allplayers;
            [{publicVariable "CP_mutiny"}] remoteExec ["BIS_fnc_spawn", 2, false];
            sleep 2;

            if (CP_mutiny > (_numberPlayers/2)) then {
                [format ["Mutiny succeed, the commander has been kicked. %1 is the new commander", name player]] remoteExec ["MCC_fnc_broadcastWoosh", 0, false];
                MCC_server setVariable [format ["CP_commander%1",(player getVariable ["CP_side",  playerside])],getPlayerUID player, true];

                //Handle radio channel side
                [player, false, (missionNamespace getVariable ["MCC_radioChannel_1",1])] remoteExec ["MCC_fnc_assignChannelServer", 2, false];
                [player, true, (missionNamespace getVariable ["MCC_radioChannel_1",1])] remoteExec ["MCC_fnc_assignChannelServer", 2, false];
            } else {
                ["Mutiny failed"] remoteExec ["MCC_fnc_broadcastWoosh", 0, false];
            }
        }
        else {
            [9999,format ["You can only start mutiny once every 5 minutes. Time to wait %1 seconds", floor (_lastMutiny - time)],3,true] spawn MCC_fnc_setIDCText;
        };
    };
};
// Run main initialization after engine/UI/network are ready
[] spawn {
    // Small delay to ensure postInit context is fully ready
    uiSleep 0.01;
    if ( isClass (configFile >> "CfgPatches" >> "mcc_sandbox") ) then {
        [] execVM "\mcc_sandbox_mod\init.sqf";
    } else {
        [] execVM "init.sqf";
    };
};



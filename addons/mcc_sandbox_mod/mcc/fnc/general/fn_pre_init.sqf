
// Set flag only in preInit; heavy initialization moved to postInit to avoid load-time blocking
if ( isClass (configFile >> "CfgPatches" >> "mcc_sandbox") ) then {
    mcc_sandbox = true;
};

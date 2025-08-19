// Wrapper that forwards to the new canonical implementation
private _fn = compile preprocessFileLineNumbers format ["%1mcc\\general_scripts\\console\\consoleOpenMenu_impl.sqf", MCC_path];
_this call _fn;



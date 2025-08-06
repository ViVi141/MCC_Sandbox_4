class general
{
    #ifdef MCCMODE
    file = "\mcc_sandbox_mod\mcc\fnc\general";
    class pre_init
    {
        preInit = 1;
        description = "STR_MCC_GENERAL_PRE_INIT";
    };
    #else
    file = "mcc\fnc\general";
    #endif

    class login {};
    class activateAddons {preInit = 1; description = "STR_MCC_GENERAL_ACTIVATEADDONS";};
    class gear {preInit = 1; description = "STR_MCC_GENERAL_GEAR";};

    class mobileRespawn {description = "STR_MCC_GENERAL_MOBILERESPAWN";};
    class buildingPosCount {description = "STR_MCC_GENERAL_BUILDINGPOSCOUNT";};
    class makeUnitsArray {description = "STR_MCC_GENERAL_MAKEUNITSARRAY";};
    class countGroup {description = "STR_MCC_GENERAL_COUNTGROUP";};
    class PiPOpen {description = "STR_MCC_GENERAL_PIPOPEN";};
    class time2String {description = "STR_MCC_GENERAL_TIME2STRING";};
    class time {description = "STR_MCC_GENERAL_TIME";};
    class setVehicleInit {description = "STR_MCC_GENERAL_SETVEHICLEINIT";};
    class setVehicleName {description = "STR_MCC_GENERAL_SETVEHICLENAME";};
    class setTime {description = "STR_MCC_GENERAL_SETTIME";};
    class setWeather {description = "STR_MCC_GENERAL_SETWEATHER";};
    class globalSay3D {description = "STR_MCC_GENERAL_GLOBALSAY3D";};
    class globalHint {description = "STR_MCC_GENERAL_GLOBALHINT";};
    class globalExecute {description = "STR_MCC_GENERAL_GLOBALEXECUTE";};
    class groupChat {description = "STR_MCC_GENERAL_GROUPCHAT";};
    class moveToPos {description = "STR_MCC_GENERAL_MOVETOPOS";};
    class pickItem {description = "STR_MCC_GENERAL_PICKITEM";};
    class broadcast {description = "STR_MCC_GENERAL_BROADCAST";};
    class paradrop {description = "STR_MCC_GENERAL_PARADROP";};
    class realParadrop {description = "STR_MCC_GENERAL_REALPARADROP";};
    class realParadropPlayer {description = "STR_MCC_GENERAL_REALPARADROPPLAYER";};
    class countGroupHC {description = "STR_MCC_GENERAL_COUNTGROUPHC";};
    class manageWp {description = "STR_MCC_GENERAL_MANAGEWP";};
    class sync {description = "STR_MCC_GENERAL_SYNC";};
    class objectMapper {description = "STR_MCC_GENERAL_OBJECTMAPPER";};
    class findRoadsLeadingZone {description = "STR_MCC_GENERAL_FINDROADSLEADINGZONE";};
    class nearestRoad {description = "STR_MCC_GENERAL_NEARESTROAD";};
    class garrison {description = "STR_MCC_GENERAL_GARRISON";};
    class saveToSQM {description = "STR_MCC_GENERAL_SAVETOSQM";};
    class saveToMCC {description = "STR_MCC_GENERAL_SAVETOMCC";};
    class loadFromMCC {description = "STR_MCC_GENERAL_LOADFROMMCC";};
    class saveToComp {description = "STR_MCC_GENERAL_SAVETOCOMP";};
    class replaceString {description = "STR_MCC_GENERAL_REPLACESTRING";};
    class dirToString {description = "STR_MCC_GENERAL_DIRTOSTRING";};
    class startLocations {description = "STR_MCC_GENERAL_STARTLOCATIONS";};
    class spawnGroup {description = "STR_MCC_GENERAL_SPAWNGROUP";};
    class keyToName {description = "STR_MCC_GENERAL_KEYTONAME";};
    class makeBriefing {description = "STR_MCC_GENERAL_MAKEBRIEFING";};
    class handleAddaction {description = "STR_MCC_GENERAL_HANDLEADDACTION";};
    class ppEffects {description = "STR_MCC_GENERAL_PPEFFECTS";};
    class SetPitchBankYaw {description = "STR_MCC_general_SetPitchBankYaw"};
    class openArtillery {description = "STR_MCC_GENERAL_PPEFFECTS"};
    class deleteBrush {description = "STR_MCC_GENERAL_PPEFFECTS"};
    class crewCount {description = "STR_MCC_GENERAL_CREWCOUNT";};
    class addVelocity {description = "STR_MCC_GENERAL_ADDVELOCITY";};
    class makeTask {description = "STR_MCC_GENERAL_MAKETASK";};
    class halt {description = "STR_MCC_GENERAL_HALT";};
};

class ied
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\ied";
	#else
	file = "mcc\fnc\ied";
	#endif

	class IedFakeExplosion	{description = "Create a fake explosion.";};
	class IedDeadlyExplosion	{description = "Create a deadly explosion.";};
	class IedDisablingExplosion	{description = "Create a disabling explosion.";};
	class ACSingle	{description = "Create an armed civilian at the given position.";};
	class trapSingle	{description = "Create an IED at the given position.";};
	class iedHit		{description = "Determine what will happened when an IED got hit.";};
	class ambushSingle	{description = "Create an ambush group.";};
	class createIED		{description = "Create the IED mechanic.";};
	class manageAmbush	{description = "Manage ambush behavior in a group.";};
	class manageAC		{description = "Manage armed civilian behavior.";};
	class SBSingle		{description = "Place suicide bomber.";};
	class manageSB		{description = "Manage SB bomber behavior.";};
	class mineSingle	{description = "Create a mine field.";};
	class iedSync {};
};

class cas
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\cas";
	#else
	file = "mcc\fnc\cas";
	#endif

	class CreateAmmoDrop	{description = "drop an object from a plane and attach paracute to it, thanks to BIS.";};
	class createPlane		{description = "create a flying plane from the given type and return the plane , pilot and group.";};
	class deletePlane		{description = "set a plane to move to a location and delete it once it come closer then 800 meters.";};
	class airDrop		{description = "Handles CAS and airdrop requests on the server";};
	class uavDetect {};
	class cas {description = "Simulate Zeus CAS with moded vehicles";};
};

class artillery
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\artillery";
	#else
	file = "mcc\fnc\artillery";
	#endif

	class CBU	{description = "drop a bomb that explode to some skeets with paracute the explode to some kind of CBU.";};
	class SADARM	{description = "drop a bomb that explode to some skeets that will search and destroy near by armor.";};
	class artyBomb	{description = "Create artillery strike with sounds on given spot.";};
	class artyFlare	{description = "Create a flare.";};
	class artyDPICM	{description = "Create DPICM artillery barage.";};
	class amb_Art	{description = "Create ambient artillery barage.";};
	class calcSolution	{description = "calculate artillery solution high or low";};
	class artyGetSolution	{description = "Broadcast artillery solution high or low";};
	class consoleFireArtillery	{description = "Broadcast artillery to artillery units";};
	class artillery {};
};

class groupGen
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\groupGen";
	#else
	file = "mcc\fnc\groupGen";
	#endif

	class groupGenRefresh	{description = "Refresh the group gen markers";};
	class groupSpawn		{description = "Create a group on the server";};
	class groupGenUMRefresh	{description = "Refresh the group gen units lists";};
};

class console
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\console";
	#else
	file = "mcc\fnc\console";
	#endif

	class consoleClickGroupIcon	{description = "Define icon behaviot when clicked on the MCC Console";};
};

class mp
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\mp";
	#else
	file = "mcc\fnc\mp";
	#endif

	class vote	{description = "Start a voting process.";};
	class getActiveSides	{description = "Return an array of the active sides in a role selection game.";};
	class PDAcreatemarker	{description = "Creates markers on mp per side and delete them after a period of time";};
	class construction		{description = "Constract a tactical building on the server side";};
	class construct_base	{description = "Constract a building in base";};
	class addRating			{description = "Adds rating to a specific player";};
	class radioSupport		{description = "Broadcast radio support to all elements not including the broadcaster group";};
	class inidbGet	{};
	class inidbSet 	{};
	class handleDB {};
	class saveServer {description = "Save persistent data about the server to the server";};
	class loadServer {description = "Load persistent data about the server from the server";};
	class savePlayer {description = "Save persistent data about the player to the server";};
	class loadPlayer {description = "Load persistent data about the player from the server";};
	class clearPersistentData {description = "Clear all data from saved files";};
};

class actions
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\actions";
	#else
	file = "mcc\fnc\actions";
	#endif

	class ilsChilds		{description = "Handles ILS childs";};
	class dragObject	{description = "Start a dragging animation must be run local on the dragging unit";};
	class releaseObject	{description = "stop a dragging animation must be run local on the dragging unit";};
	class releasePod	{description = "Release a pod from Taru helicopter";};
	class attachPod		{description = "Attach a pod to Taru helicopter";};
	class vault			{description = "Vault over an obstacle";};
	class cover			{description = "Manage cover mechanics";};
	class coverInit		{preInit = 1; description = "Init Cover System";};
	class weaponSelect	{description = "Change weapons and throw utility";};
	class utilityUse	{description = "use utility";};
	class grenadeThrow	{description = "Throw grenades";};
	class pickKit		{description = "pick up dead unit kit";};
	class canAttachPod	{description = "check if can attach pod";};
	class addILSChildrenACE {description = "Add ILS actions to ACE ui";};
	class spotEnemy {description = "spot an enmey from ACE menu";};
	class callSupport {description = "Call support from ACE menu";};
	class callConstruct {description = "Call construct from ACE menu";};
	class resupply {description = "Resupply ammo from an ammo box";};
	class breakdown {description = "Breakdown MCC crate into supplies";};
	class ACEdropAmmobox {description = "Drop MCC ammbox in ACE";};
};

class evac
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\evac";
	#else
	file = "mcc\fnc\evac";
	#endif

	class evacDelete {description = "Delete the given vehicle or it's driver";};
	class evacMove {description = "Move a vehicle to selected WP";};
	class evacSpawn {description = "Spawn a vehicle with crew and gunners, mark it as an evac vehicle";};
	class repairEvac {description = "Repair evac helicopter";};
	class setEvac {description = "Sets an empty ot AI vehicle into an ecav for a specific side";};
	class fastRopeLocal {description = "handles fast rope on clients";};
};

class dynamicDialog
{
	#ifdef MCCMODE
	file = "\mcc_sandbox_mod\mcc\fnc\dynamicDialog";
	#else
	file = "mcc\fnc\dynamicDialog";
	#endif

	class initDynamicDialog {description = "init the dynamic dialog";};
};
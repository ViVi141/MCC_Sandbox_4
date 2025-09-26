#define UNIT_TYPE 3010
#define UNIT_CLASS 3011
#define MCC_GGUNIT_TYPE 3012
#define MCC_GGUNIT_BEHAVIOR 3030
#define MCC_GroupGenCurrentGroup_IDD 9003
#define MCC_GGListBoxIDC 3013
#define MCC_GGADDIDC 3014
#define MCC_GGCLEARIDC 3015
#define MCC_GGUNIT_EMPTY 3016
#define MCC_GGUNIT_EMPTYTITLE 3017
#define mcc_groupGen_CurrentgroupNameTittle_IDC 3018
#define mcc_groupGen_CurrentgroupNameText_IDC 3019
#define MCC_GGSAVE_GROUPIDC 3020
#define MCC_GGVREATE_IDC 3021

class MCC_spawnDialogControls:MCC_RscControlsGroup
{
	idc = 506;
	x = 0.186 * safezoneW + safezoneX;
	y = 0.095 * safezoneH + safezoneY;
	w = 0.360938 * safezoneW;
	h = 0.30788 * safezoneH;

	class Controls
	{
			
		class MCC_spawnDialogFrame: MCC_RscText
		{
			idc = -1;
			colorBackground[] = {0,0,0,0.9};
			
			w = 0.360938 * safezoneW;
			h = 0.30788 * safezoneH;
		};

		class mcc_groupGen_SpawnTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_SPAWN_TITLE";
			colorText[] = {0,1,1,1};
			
			x = 0.103125 * safezoneW;
			y =0.0109958 * safezoneH;
			w = 0.108854 * safezoneW;
			h = 0.0329871 * safezoneH;
		};

		class mcc_groupGen_typeTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_TYPE";
			x = 0.00572967 * safezoneW;
			y = 0.0549786 * safezoneH;
			w = 0.045 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_typeComboBox: MCC_RscCombo
		{
			idc = MCC_GGUNIT_TYPE;
			onLBSelChanged = __EVAL("[3] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\group_change.sqf'");

			x = 0.0572917 * safezoneW;
			y = 0.0549786 * safezoneH;
			w = 0.120313 * safezoneW;
			h = 0.0260715 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_BranchTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_BRANCH";
			x = 0.00572967 * safezoneW;
			y = 0.0879657 * safezoneH;
			w = 0.045 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_branchComboBox: MCC_RscCombo
		{
			idc = UNIT_TYPE;
			onLBSelChanged = __EVAL("[0] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\group_change.sqf'");

			x = 0.0572917 * safezoneW;
			y = 0.0879657 * safezoneH;
			w = 0.120313 * safezoneW;
			h = 0.0260715 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_classTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_CLASS";
			x = 0.00572967 * safezoneW;
			y = 0.120953 * safezoneH;
			w = 0.045 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_classComboBox: MCC_RscCombo
		{
			idc = UNIT_CLASS;

			x = 0.0572917 * safezoneW;
			y = 0.120953 * safezoneH;
			w = 0.120313 * safezoneW;
			h = 0.0260715 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_BehaviorTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_BEHAVIOR";
			x = 0.00572967 * safezoneW;
			y = 0.15394 * safezoneH;
			w = 0.045 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_BehaviorComboBox: MCC_RscCombo
		{
			idc = MCC_GGUNIT_BEHAVIOR;

			x = 0.0572917 * safezoneW;
			y = 0.15394 * safezoneH;
			w = 0.120313 * safezoneW;
			h = 0.0260715 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_EmptyTittle: MCC_RscText
		{
			idc = MCC_GGUNIT_EMPTYTITLE;

			text = "$STR_MCC_GROUPGEN_EMPTY";
			x = 0.00572967 * safezoneW;
			y = 0.186927 * safezoneH;
			w = 0.045 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_EmptyComboBox: MCC_RscCombo
		{
			idc = MCC_GGUNIT_EMPTY;

			x = 0.0572917 * safezoneW;
			y = 0.186927 * safezoneH;
			w = 0.120313 * safezoneW;
			h = 0.0260715 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_CurrentgroupListBox: MCC_RscListbox
		{
			idc = MCC_GroupGenCurrentGroup_IDD;
			colorBorder[] = {1,1,1,1};

			x = 0.257813 * safezoneW;
			y = 0.0879657 * safezoneH;
			w = 0.0973958 * safezoneW;
			h = 0.109957 * safezoneH;
		};
		class mcc_groupGen_CurrentgroupNameTittle: MCC_RscText
		{
			idc = mcc_groupGen_CurrentgroupNameTittle_IDC;

			text = "$STR_MCC_GROUPGEN_NAME";
			x = 0.257813 * safezoneW;
			y = 0.0549786 * safezoneH;
			w = 0.034375 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class mcc_groupGen_CurrentgroupNameText: MCC_RscText
		{
			idc = mcc_groupGen_CurrentgroupNameText_IDC;
			type = 2;

			x = 0.292188 * safezoneW;
			y = 0.0549786 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};
		class mcc_groupGen_classAddButton: MCC_RscButton
		{
			idc = MCC_GGADDIDC;
			onButtonClick = __EVAL("[1] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\group_change.sqf'");
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.9)";

			text = "$STR_MCC_GROUPGEN_ADD_TO_LIST";
			x = 0.183334 * safezoneW;
			y = 0.0549786 * safezoneH;
			w = 0.065625 * safezoneW;
			h = 0.035 * safezoneH;
			tooltip = "$STR_MCC_ADD_TO_LIST_TOOLTIP";
		};
		class mcc_groupGen_groupListBoxClearButton: MCC_RscButton
		{
			idc = MCC_GGCLEARIDC;
			onButtonClick = __EVAL("[2] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\group_change.sqf'");

			text = "$STR_MCC_GROUPGEN_CLEAR_LIST";
			x = 0.183334 * safezoneW;
			y = 0.098962 * safezoneH;
			w = 0.065625 * safezoneW;
			h = 0.035 * safezoneH;
			tooltip = "$STR_MCC_CLEAR_LIST_TOOLTIP";
		};
		class mcc_groupGen_groupListSaveButton: MCC_RscButton
		{
			idc = MCC_GGSAVE_GROUPIDC;
			onButtonClick = __EVAL("[4] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\group_change.sqf'");

			text = "$STR_MCC_SAVE_AS_CUSTOM";
			x = 0.292188 * safezoneW;
			y = 0.208919 * safezoneH;
			w = 0.065625 * safezoneW;
			h = 0.035 * safezoneH;
			tooltip = "$STR_MCC_SAVE_AS_CUSTOM_TOOLTIP";
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class mcc_groupGen_groupListBoxCreaterButton: MCC_RscButton
		{
			idc = MCC_GGVREATE_IDC;
			onButtonClick = __EVAL("[0] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\spawn_request.sqf'");

			text = "$STR_MCC_CREATE";
			x = 0.183334 * safezoneW;
			y = 0.164936 * safezoneH;
			w = 0.065625 * safezoneW;
			h = 0.035 * safezoneH;
			tooltip = "$STR_MCC_CREATE_TOOLTIP";
		};
		class mcc_groupGen_groupListBoxAddToZoneButton: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL("[1] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\spawn_request.sqf'");
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.9)";

			text = "$STR_MCC_SPAWN_IN_ZONE";
			x = 0.183334 * safezoneW;
			y = 0.208919 * safezoneH;
			w = 0.065625 * safezoneW;
			h = 0.035 * safezoneH;
			tooltip = "$STR_MCC_SPAWN_IN_ZONE_TOOLTIP";
		};
		class MCC_zoneLocTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_LOCATION";
			x = 0.00572967 * safezoneW;
			y = 0.219914 * safezoneH;
			w = 0.045 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		class MCC_zoneLoc: MCC_RscCombo
		{
			idc = 0;
			onLBSelChanged = "mcc_hc = (MCC_ZoneLocation select (lbCurSel (_this select 0))) select 1;";

			x = 0.0572917 * safezoneW;
			y = 0.219914 * safezoneH;
			w = 0.120313 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		
		class MCC_delayedSpawnText: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_DELAYED";
			x = 0.00572967 * safezoneW;
			y = 0.26 * safezoneH;
			w = 0.045 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		
		class MCC_delayedCacheText: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_CACHE";
			x = 0.09 * safezoneW;
			y = 0.26 * safezoneH;
			w = 0.045 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};
		
		class MCC_delayedSpawn: MCC_RscCheckbox
		{
			idc = 3022;
			tooltip = "Units will not spawn until players are nearby";
			x = 0.05 * safezoneW;
			y = 0.26 * safezoneH;
			w = 0.0171875 * safezoneW;
			h = 0.022 * safezoneH;
		};
		
		class MCC_CacheSpawn: MCC_RscCheckbox
		{
			idc = 3023;
			tooltip = "Units will spawn and cache automatically";
			x = 0.13 * safezoneW;
			y = 0.26 * safezoneH;
			w = 0.0171875 * safezoneW;
			h = 0.022 * safezoneH;
		};

		class mcc_groupGen_spawnCloseButton: MCC_RscButtonMenu
		{
			idc = -1;
			onButtonClick = "_mccdialog = (uiNamespace getVariable 'MCC_groupGen_Dialog');(_mccdialog displayCtrl 506) ctrlShow false; mcc_delayed_spawn = if (cbChecked  (_mccdialog displayctrl 3022)) then {true} else {false};mcc_caching = if (cbChecked  (_mccdialog displayctrl 3023)) then {true} else {false};";
			text = "$STR_MCC_CLOSE";
			
			x = 0.166146 * safezoneW;
			y = 0.263897 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0329871 * safezoneH;
		};
	};
};
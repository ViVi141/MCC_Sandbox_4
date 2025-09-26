#define MCC_TRAPS_TYPE 2007
#define MCC_TRAPS_OBJECT 2008
#define MCC_TRAPS_EXPLOSIN_SIZE 2009
#define MCC_TRAPS_EXPLOSIN_TYPE 2010
#define MCC_TRAPS_TARGET_FACTION 2011
#define MCC_TRAPS_JAMMABLE 2012
#define MCC_TRAPS_DISARM 2013
#define MCC_TRAPS_TRIGGER 2014
#define MCC_TRAPS_PROXIMITY 2015
#define MCC_TRAPS_AMBUSH 2016

class MCC_IEDDialogControls:MCC_RscControlsGroup
{
	idc = 508;
	x = 0.186 * safezoneW + safezoneX;
	y = 0.18 * safezoneH + safezoneY;
	w = 0.303646 * safezoneW;
	h = 0.43 * safezoneH;

	class Controls
	{
		class MCC_IEDDialogFrame: MCC_RscText
		{
			idc = -1;
			colorBackground[] = {0,0,0,0.9};

			w = 0.303646 * safezoneW;
			h = 0.30788 * safezoneH;
		};

		class MCC_trapsTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_IED_TITLE";
			x = 0.114584 * safezoneW;
			y = 0.0109958 * safezoneH;
			w = 0.09 * safezoneW;
			h = 0.0340016 * safezoneH;
			colorText[] = {0,1,1,1};
		};
		class MCC_trapsTypeTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_TYPE";
			x = 0.00572965 * safezoneW;
			y = 0.0989618 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsObjectTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_IED_OBJECT";
			x = 0.00572965 * safezoneW;
			y = 0.131949 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsExplosionSizeTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_IED_SIZE";
			x = 0.00572965 * safezoneW;
			y = 0.164936 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsExplosionTypeTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_IED_TYPE";
			x = 0.00572965 * safezoneW;
			y = 0.197923 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsDisarmDurationTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_IED_DISARM_TIME";
			x = 0.160417 * safezoneW;
			y = 0.131949 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsJammableTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_IED_JAMMABLE";
			x = 0.160417 * safezoneW;
			y = 0.0989618 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsTargetFactionTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_IED_TARGET_FACTION";
			x = 0.00572965 * safezoneW;
			y = 0.23091 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsTriggerTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_GROUPGEN_IED_TRIGGER_TYPE";
			x = 0.160417 * safezoneW;
			y = 0.164936 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsProximityTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_IED_PROXIMITY";
			x = 0.160417 * safezoneW;
			y = 0.197923 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsAmbushGroupTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_IED_AMBUSH_GROUP";
			x = 0.160417 * safezoneW;
			y = 0.23091 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsType: MCC_RscCombo
		{
			idc = MCC_TRAPS_TYPE;
			onLBSelChanged = __EVAL("[0] execVM '"+MCCPATH+"mcc\fnc\ied\scripts\trap_change.sqf'");

			x = 0.0802087 * safezoneW;
			y = 0.0989618 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsObject: MCC_RscCombo
		{
			idc = MCC_TRAPS_OBJECT;

			x = 0.0802087 * safezoneW;
			y = 0.131949 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsExplosionSize: MCC_RscCombo
		{
			idc = MCC_TRAPS_EXPLOSIN_SIZE;

			x = 0.0802087 * safezoneW;
			y = 0.164936 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsExplosionType: MCC_RscCombo
		{
			idc = MCC_TRAPS_EXPLOSIN_TYPE;

			x = 0.0802087 * safezoneW;
			y = 0.197923 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsTargetFaction: MCC_RscCombo
		{
			idc = MCC_TRAPS_TARGET_FACTION;

			x = 0.0802087 * safezoneW;
			y = 0.23091 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsJammable: MCC_RscCheckBox
		{
			idc = MCC_TRAPS_JAMMABLE;

			x = 0.234896 * safezoneW;
			y = 0.0989618 * safezoneH;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsDisarm: MCC_RscCombo
		{
			idc = MCC_TRAPS_DISARM;

			x = 0.234896 * safezoneW;
			y = 0.131949 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsTrigger: MCC_RscCombo
		{
			idc = MCC_TRAPS_TRIGGER;

			x = 0.234896 * safezoneW;
			y = 0.164936 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsProximity: MCC_RscCombo
		{
			idc = MCC_TRAPS_PROXIMITY;

			x = 0.234896 * safezoneW;
			y = 0.197923 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsAmbushGroup: MCC_RscCombo
		{
			idc = MCC_TRAPS_AMBUSH;

			x = 0.234896 * safezoneW;
			y = 0.23091 * safezoneH;
			w = 0.0630208 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsCreateIED: MCC_RscButton
		{
			idc = -1;
			onButtonClick =  __EVAL("[0] execVM '"+MCCPATH+"mcc\fnc\ied\scripts\trap_request.sqf'");

			text = "$STR_MCC_CREATE_IED";
			x = 0.154688 * safezoneW;
			y = 0.263897 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0329871 * safezoneH;
			tooltip = "$STR_MCC_CREATE_IED_TOOLTIP";
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsCreateAmbush: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL("[1] execVM '"+MCCPATH+"mcc\fnc\ied\scripts\trap_request.sqf'");

			text = "$STR_MCC_CREATE_AMBUSH";
			x = 0.229167 * safezoneW;
			y = 0.263897 * safezoneH;
			w = 0.06875 * safezoneW;
			h = 0.0329871 * safezoneH;
			tooltip = "$STR_MCC_CREATE_AMBUSH_TOOLTIP";
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.65)";
		};
		class MCC_trapsExplainTittle: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_IED_INSTRUCTIONS_1";
			x = 0.00572965 * safezoneW;
			y = 0.0301928 * safezoneH;
			w = 0.3 * safezoneW;
			h = 0.0329871 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.58)";
		};
		class MCC_trapsExplainTittle2: MCC_RscText
		{
			idc = -1;

			text = "$STR_MCC_IED_INSTRUCTIONS_2";
			x = 0.00572965 * safezoneW;
			y = 0.0548928 * safezoneH;
			w = 0.3 * safezoneW;
			h = 0.0329871 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.58)";
		};
		class MCC_trapsCloseButton: MCC_RscButtonMenu
		{
			idc = -1;
			onButtonClick = "((uiNamespace getVariable 'MCC_groupGen_Dialog') displayCtrl 508) ctrlShow false";

			text = "$STR_MCC_CLOSE";
			x = 0.00572965 * safezoneW;
			y = 0.263897 * safezoneH;
			w = 0.06799 * safezoneW;
			h = 0.0340016 * safezoneH;
		};
	};
};
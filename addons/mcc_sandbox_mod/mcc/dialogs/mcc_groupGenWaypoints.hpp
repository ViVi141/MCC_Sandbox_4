#define MCC_GroupGenWPCombo_IDC 9015
#define MCC_GroupGenWPformationCombo_IDC 9016
#define MCC_GroupGenWPspeedCombo_IDC 9017
#define MCC_GroupGenWPbehaviorCombo_IDC 9018

class MCC_waypointsDialogControls:MCC_RscControlsGroup
{
	idc = 510;
	x = 0.1 * safezoneW + safezoneX;
	y = 0.1 * safezoneH + safezoneY;
	w = 0.189063 * safezoneW;
	h = 0.219914 * safezoneH;

	class Controls
	{	

		class MCC_GroupGenInfoText: MCC_RscText
		{
			idc = -1;
			colorBackground[] = {0,0,0,0.9};

			w = 0.189063 * safezoneW;
			h = 0.219914 * safezoneH;
		};
		
		class MCC_GroupGenWPTittle: MCC_RscText
		{
			idc = -1;
			text = "$STR_MCC_WAY_POINTS";
			colorText[] = {0,1,1,1};
			
			x = 0.0630206 * safezoneW;
			y = 0.0109958 * safezoneH;
			w = 0.0916667 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
		
		class MCC_GroupGenWPCombo: MCC_RscCombo
		{
			idc = MCC_GroupGenWPCombo_IDC;

			x = 0.0744797 * safezoneW;
			y = 0.0439828 * safezoneH;
			w = 0.108854 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
		
		class MCC_GroupGenWPformationCombo: MCC_RscCombo
		{
			idc = MCC_GroupGenWPformationCombo_IDC;

			x = 0.0744797 * safezoneW;
			y = 0.0769698 * safezoneH;
			w = 0.108854 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
		class MCC_GroupGenWPspeedCombo: MCC_RscCombo
		{
			idc = MCC_GroupGenWPspeedCombo_IDC;

			x = 0.0744797 * safezoneW;
			y = 0.109957 * safezoneH;
			w = 0.108854 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
		class MCC_GroupGenWPbehaviorCombo: MCC_RscCombo
		{
			idc = MCC_GroupGenWPbehaviorCombo_IDC;

			x = 0.0744797 * safezoneW;
			y = 0.142944 * safezoneH;
			w = 0.108854 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
		class MCC_GroupGenWPAdd: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL("[0] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\manageWP.sqf'");

			text = "$STR_MCC_ADD";
			x = 0.0687497 * safezoneW;
			y = 0.175932 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0329871 * safezoneH;
			tooltip = "$STR_MCC_ADD_WAYPOINT_TOOLTIP";
		};
		class MCC_GroupGenWPReplace: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL("[1] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\manageWP.sqf'");

			text = "$STR_MCC_REPLACE";
			x = 0.131771 * safezoneW;
			y = 0.175932 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0329871 * safezoneH;
			tooltip = "$STR_MCC_REPLACE_WAYPOINT_TOOLTIP";
		};
		class MCC_GroupGenWPClear: MCC_RscButton
		{
			idc = -1;
			onButtonClick = __EVAL("[2] execVM '"+MCCPATH+"mcc\general_scripts\groupGen\manageWP.sqf'");

			text = "$STR_MCC_CLEAR";
			x = 0.00572965 * safezoneW;
			y = 0.175932 * safezoneH;
			w = 0.0515625 * safezoneW;
			h = 0.0329871 * safezoneH;
			tooltip = "$STR_MCC_CLEAR_WAYPOINT_TOOLTIP";
		};
		class MCC_GroupGenWPTypeTittle: MCC_RscText
		{
			idc = -1;
			text = "$STR_MCC_TYPE";
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.85)";
			
			x = 0.00572965 * safezoneW;
			y = 0.0439828 * safezoneH;
			w = 0.0572917 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
		class MCC_GroupGenWPFormationTittle: MCC_RscText
		{
			idc = -1;
			text = "$STR_MCC_FORMATION";
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.85)";
			
			x = 0.00572965 * safezoneW;
			y = 0.0769698 * safezoneH;
			w = 0.0572917 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
		class MCC_GroupGenWPspeedTittle: MCC_RscText
		{
			idc = -1;
			text = "$STR_MCC_WP_SPEED";
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.85)";
			
			x = 0.00572965 * safezoneW;
			y = 0.109957 * safezoneH;
			w = 0.0572917 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
		class MCC_GroupGenWPbehaviorTittle: MCC_RscText
		{
			idc = -1;
			text = "$STR_MCC_WP_BEHAVIOR";
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.85)";
			
			x = 0.00572965 * safezoneW;
			y = 0.142944 * safezoneH;
			w = 0.0572917 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
	};
};


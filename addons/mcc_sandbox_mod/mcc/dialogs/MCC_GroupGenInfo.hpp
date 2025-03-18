#define MCC_GroupGenInfoText_IDC 9013
#define MCC_GroupGenInfo_IDC 530
#define MCC_GroupGenInfo_zone_IDC 5311
#define MCC_GroupGenInfo_gaiaBehaviorCombo_IDC 5312
#define MCC_GroupGenInfo_gaiaBehaviorButton_IDC 5313
#define MCC_GroupGenInfo_gaiaRespawnCombo_IDC 5314
#define MCC_GroupGenInfo_gaiaRespawnComboButton_IDC 5315
#define MCC_GroupGenInfo_giveToPlayer_IDC 5316
#define MCC_GroupGenInfo_cacheButton_IDC 5317


class MCC_GroupGenInfo:MCC_RscControlsGroup
{
	idc = MCC_GroupGenInfo_IDC;
	x = 0.1 * safezoneW + safezoneX;
	y = 0.1 * safezoneH + safezoneY;
	w = 0.18 * safezoneW;
	h = 0.2 * safezoneH;

	class Controls
	{
		class MCC_GroupGenInfoText2: MCC_RscText
		{
			idc = 9013111;
			colorBackground[] = {0,0,0,0.95};
			w = 0.17 * safezoneW;
			h = 0.23 * safezoneH;
		};

		class MCC_GroupGenInfoText: MCC_RscStructuredText
		{
			idc = MCC_GroupGenInfoText_IDC;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.5)";
			colorBackground[] = {0,0,0,0.95};

			w = 0.17 * safezoneW;
			h = 0.23 * safezoneH;
		};

		class MCC_GroupGenInfo_zone: MCC_RscCombo
		{
			idc = MCC_GroupGenInfo_zone_IDC;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
			onLBSelChanged = "MCC_GAIAIntendZone = str ((lbcurSel (_this select 0))+1)";

			w = 0.0458333 * safezoneW;
			h = 0.0219914 * safezoneH;
		};

		class MCC_GroupGenInfo_gaiaBehaviorCombo: MCC_RscCombo
		{
			idc = MCC_GroupGenInfo_gaiaBehaviorCombo_IDC;
			onLBSelChanged = "MCC_behavior_index = (lbcurSel (_this select 0))";

			w = 0.06875 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};

		class MCC_GroupGenInfo_gaiaBehaviorButton: MCC_RscButton
		{
			idc = MCC_GroupGenInfo_gaiaBehaviorButton_IDC;
			onButtonClick = "if (!isnil 'MCC_GroupGenGroupSelected') then {if (count MCC_GroupGenGroupSelected > 0) then {{_x setVariable ['GAIA_ZONE_INTEND',[MCC_GAIAIntendZone ,((MCC_spawn_behaviors select MCC_behavior_index) select 1)], true]}foreach MCC_GroupGenGroupSelected}};";

			text = "GAIA"; //--- ToDo: Localize;

			w = 0.0572917 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "将所选组与所选区域和行为交给GAIA控制"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};

		class MCC_GroupGenInfo_gaiaRespawnCombo: MCC_RscCombo
		{
			idc = MCC_GroupGenInfo_gaiaRespawnCombo_IDC;
			onLBSelChanged = "MCC_GAIARespawnNumberIndex = if ((lbcurSel (_this select 0))>10) then {999} else {(lbcurSel (_this select 0))}";

			w = 0.0458333 * safezoneW;
			h = 0.0219914 * safezoneH;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.8)";
		};

		class MCC_GroupGenInfo_gaiaRespawnComboButton: MCC_RscButton
		{
			idc = MCC_GroupGenInfo_gaiaRespawnComboButton_IDC;
			onButtonClick = "if (!isnil 'MCC_GroupGenGroupSelected') then {if (count MCC_GroupGenGroupSelected > 0) then {{[_x,MCC_GAIARespawnNumberIndex] spawn GAIA_fnc_respawnSet}foreach MCC_GroupGenGroupSelected}};";

			text = "Respawns"; //--- ToDo: Localize;

			w = 0.06 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "重生超过0的组如果被取消，将继续重生"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};

		class  MCC_GroupGenInfo_giveToPlayer: MCC_RscButton
		{
			idc = MCC_GroupGenInfo_giveToPlayer_IDC;
			onButtonClick = "if (!isnil 'MCC_GroupGenGroupSelected') then {if (count MCC_GroupGenGroupSelected > 0) then {{_x setVariable ['MCC_canbecontrolled',true,true]; _x setVariable ['GAIA_ZONE_INTEND',[],true]}foreach MCC_GroupGenGroupSelected}};";

			text = "Player"; //--- ToDo: Localize;
			w = 0.0572917 * safezoneW;
			h = 0.0219914 * safezoneH;
			tooltip = "通过M-Tac MCC手持控制台将所选组交给玩家控制"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";
		};

		class MCC_GroupGenInfo_cacheButton: MCC_RscButton
		{
			idc = MCC_GroupGenInfo_cacheButton_IDC;
			onButtonClick = "if (!isnil 'MCC_GroupGenGroupSelected') then {if (count MCC_GroupGenGroupSelected > 0) then {{_x setVariable ['mcc_gaia_cache', !(_x getVariable ['mcc_gaia_cache',false]),true];}foreach MCC_GroupGenGroupSelected}};";
			tooltip = "将所选组交给缓存系统";
			text = "Cache"; //--- ToDo: Localize;
			sizeEx = "(((((safezoneW / safezoneH) min 1.2) / 1.2) / 25) * 0.7)";

			w = 0.0744792 * safezoneW;
			h = 0.0219914 * safezoneH;
		};
	};
};
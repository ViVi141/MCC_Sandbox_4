class MCC_PerformancePresets {
	idd = 12347;
	movingEnable = false;
	onLoad = "[] call MCC_fnc_openPerformancePresets";
	
	class controlsBackground {
		class Background: MCC_RscText {
			idc = -1;
			x = 0.3 * safezoneW + safezoneX;
			y = 0.2 * safezoneH + safezoneY;
			w = 0.4 * safezoneW;
			h = 0.7 * safezoneH;
			colorBackground[] = {0,0,0,0.8};
		};
		
		class Title: MCC_RscText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_PRESETS_TITLE";
			x = 0.3 * safezoneW + safezoneX;
			y = 0.2 * safezoneH + safezoneY;
			w = 0.4 * safezoneW;
			h = 0.05 * safezoneH;
			colorBackground[] = {0,0,0,0.9};
			colorText[] = {1,1,1,1};
			sizeEx = 0.04;
		};
	};
	
	class controls {
		// Low Performance
		class LowButton: MCC_RscButton {
			idc = 3001;
			text = "$STR_MCC_PERFORMANCE_LOW";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.27 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.06 * safezoneH;
			colorBackground[] = {0.8,0.2,0.2,0.8};
		};
		
		class LowDesc: MCC_RscStructuredText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_LOW_DESC";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.34 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.04 * safezoneH;
			colorText[] = {0.8,0.8,0.8,1};
		};
		
		// Medium Performance
		class MediumButton: MCC_RscButton {
			idc = 3002;
			text = "$STR_MCC_PERFORMANCE_MEDIUM";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.4 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.06 * safezoneH;
			colorBackground[] = {0.8,0.6,0.2,0.8};
		};
		
		class MediumDesc: MCC_RscStructuredText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_MEDIUM_DESC";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.47 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.04 * safezoneH;
			colorText[] = {0.8,0.8,0.8,1};
		};
		
		// High Performance
		class HighButton: MCC_RscButton {
			idc = 3003;
			text = "$STR_MCC_PERFORMANCE_HIGH";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.53 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.06 * safezoneH;
			colorBackground[] = {0.2,0.8,0.2,0.8};
		};
		
		class HighDesc: MCC_RscStructuredText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_HIGH_DESC";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.6 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.04 * safezoneH;
			colorText[] = {0.8,0.8,0.8,1};
		};
		
		// Unlimited Performance
		class UnlimitedButton: MCC_RscButton {
			idc = 3004;
			text = "$STR_MCC_PERFORMANCE_UNLIMITED";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.66 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.06 * safezoneH;
			colorBackground[] = {0.8,0.2,0.8,0.8};
		};
		
		class UnlimitedDesc: MCC_RscStructuredText {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_UNLIMITED_DESC";
			x = 0.32 * safezoneW + safezoneX;
			y = 0.73 * safezoneH + safezoneY;
			w = 0.36 * safezoneW;
			h = 0.04 * safezoneH;
			colorText[] = {0.8,0.8,0.8,1};
		};
		
		// Close Button
		class CloseButton: MCC_RscButton {
			idc = -1;
			text = "$STR_MCC_PERFORMANCE_CLOSE";
			x = 0.5 * safezoneW + safezoneX;
			y = 0.85 * safezoneH + safezoneY;
			w = 0.1 * safezoneW;
			h = 0.04 * safezoneH;
			action = "closeDialog 0;";
		};
	};
};

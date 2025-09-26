class MCC_taskMonitorDialog {
	idd = 9001;
	movingEnable = 1;
	enableSimulation = 1;
	
	class controlsBackground {
		class Background: MCC_RscText {
			idc = -1;
			x = 0.1;
			y = 0.1;
			w = 0.8;
			h = 0.8;
			colorBackground[] = {0,0,0,0.8};
		};
		
		class Title: MCC_RscText {
			idc = 1001;
			text = "MCC Task Monitor";
			x = 0.1;
			y = 0.1;
			w = 0.8;
			h = 0.05;
			colorBackground[] = {0,0.5,0,0.8};
			colorText[] = {1,1,1,1};
			sizeEx = 0.05;
		};
	};
	
	class controls {
		class StatsList: MCC_RscListbox {
			idc = 1501;
			x = 0.15;
			y = 0.2;
			w = 0.7;
			h = 0.5;
			colorBackground[] = {0,0,0,0.5};
			colorText[] = {1,1,1,1};
		};
		
		class RefreshButton: MCC_RscButton {
			idc = 1601;
			text = "Refresh";
			x = 0.15;
			y = 0.75;
			w = 0.15;
			h = 0.05;
			action = "[] call MCC_fnc_refreshTaskStats;";
		};
		
		class CleanupButton: MCC_RscButton {
			idc = 1602;
			text = "Cleanup Tasks";
			x = 0.35;
			y = 0.75;
			w = 0.15;
			h = 0.05;
			action = "[] call MCC_fnc_emergencyCleanup;";
		};
		
		class CloseButton: MCC_RscButton {
			idc = 1603;
			text = "Close";
			x = 0.55;
			y = 0.75;
			w = 0.15;
			h = 0.05;
			action = "closedialog 0;";
		};
	};
};

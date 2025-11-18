# SQF 文件括号嵌套修复报告

生成时间: 2025-11-18 13:58:32

## 统计信息

- **总文件数**: 909
- **有问题文件数**: 11
- **括号不匹配数**: 20
- **重复 if 嵌套数**: 0
- **已修复文件数**: 4
- **错误数**: 0

## 详细问题列表

### mcc\UI\fnc\fn_initCuratorAttribute.sqf

#### 括号不匹配问题

- 行 4, 列 1: unclosed (括号: {)
- 行 10, 列 75: unclosed (括号: {)

### mcc\rts\scripts\mcc_logisticsBaseBuild.sqf

#### 括号不匹配问题

- 行 1061, 列 48: 括号不匹配 (开括号: {, 闭括号: ])

### mcc\missionWizard\fnc\fn_MWObjectiveHVT.sqf

#### 括号不匹配问题

- 行 194, 列 27: 括号不匹配 (开括号: {, 闭括号: ])

### mcc\LHD\fnc\fn_LHDspawnMenuInit.sqf

#### 括号不匹配问题

- 行 262, 列 2: 括号不匹配 (开括号: {, 闭括号: ])
- 行 261, 列 25: 括号不匹配 (开括号: {, 闭括号: ])

### mcc\LHD\fnc\fn_LHDspawnVehicle.sqf

#### 括号不匹配问题

- 行 362, 列 29: 括号不匹配 (开括号: {, 闭括号: ])
- 行 354, 列 5: 括号不匹配 (开括号: [, 闭括号: })
- 行 345, 列 14: 括号不匹配 (开括号: [, 闭括号: })
- 行 345, 列 6: 括号不匹配 (开括号: [, 闭括号: })

### mcc\general_scripts\convoy\make_convoy_WP.sqf

#### 括号不匹配问题

- 行 10, 列 46: 括号不匹配 (开括号: {, 闭括号: ])

### mcc\general_scripts\hostages\create_hostage.sqf

#### 括号不匹配问题

- 行 27, 列 1: 括号不匹配 (开括号: [, 闭括号: })
- 行 40, 列 3: unexpected_closing (括号: ])
- 行 62, 列 1: unexpected_closing (括号: ])

### mcc\fnc\general\fn_keyToName.sqf

#### 括号不匹配问题

- 行 54, 列 10: unclosed (括号: {)

### mcc\fnc\general\fn_pickItem.sqf

#### 括号不匹配问题

- 行 16, 列 27: unclosed (括号: {)

### mcc\bombDefuse\fnc\fn_bdButtonsModule.sqf

#### 括号不匹配问题

- 行 24, 列 131: 括号不匹配 (开括号: [, 闭括号: ))
- 行 27, 列 101: 括号不匹配 (开括号: (, 闭括号: ])

### mcc\ambient\fnc\fn_ambientFirePlayerFiredEH.sqf

#### 括号不匹配问题

- 行 11, 列 24: 括号不匹配 (开括号: [, 闭括号: })
- 行 41, 列 8: unexpected_closing (括号: ])


## 日志

```
[2025-11-18 13:58:31] [INFO] ============================================================
[2025-11-18 13:58:31] [INFO] SQF 文件括号嵌套修复脚本
[2025-11-18 13:58:31] [INFO] ============================================================
[2025-11-18 13:58:31] [INFO] 模式: 试运行（不会实际修改文件）
[2025-11-18 13:58:31] [INFO] 开始扫描 SQF 文件...
[2025-11-18 13:58:31] [INFO] 找到 909 个 SQF 文件
[2025-11-18 13:58:31] [INFO] 正在分析: 10/909 (1%) - bon_arti_func_dlgUpdate.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 20/909 (2%) - helmetcam.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 30/909 (3%) - specta_events.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 40/909 (4%) - init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 50/909 (5%) - init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 60/909 (6%) - init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 70/909 (7%) - init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 80/909 (8%) - MCCFrontLineDialog_init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 90/909 (9%) - mcc_playerConsole_init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 100/909 (11%) - save_gear.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 110/909 (12%) - group_change3d.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 120/909 (13%) - mcc_make_array_obj.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 130/909 (14%) - mcc_extras_pv_handler.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 140/909 (15%) - respawnSettings.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 150/909 (16%) - fn_vehicleRandomAnimation.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 160/909 (17%) - fn_checkBox.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 170/909 (18%) - fn_getKeyFromCBA.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 180/909 (19%) - fn_tagSystem.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 190/909 (20%) - fn_survivalProgressBars.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 200/909 (22%) - fn_surviveWaterTreatment.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 210/909 (23%) - fn_baseSelected.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 220/909 (24%) - fn_mainBoxInit.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 230/909 (25%) - fn_rtsBuyTickets.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 240/909 (26%) - fn_rtsLoadResources.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 250/909 (27%) - fn_rtsRespawnUnits.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 260/909 (28%) - fn_vehicleSpawnerBuildCostTable.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 270/909 (29%) - fn_addWeapon.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 280/909 (30%) - fn_getVariable.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 290/909 (31%) - fn_RSTakeCommander.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 300/909 (33%) - gearPanel_init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 310/909 (34%) - fn_VONRadioBroadcast.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 320/909 (35%) - fn_campaignSpawnAIInit.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 330/909 (36%) - fn_MWCreateTask.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 340/909 (37%) - fn_MWObjectiveDisable.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 350/909 (38%) - fn_MWUpdateZone.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 360/909 (39%) - fn_loadWounded.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 370/909 (40%) - fn_cargoLoadModule.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 380/909 (41%) - mcc_logisticsLoadTruck_init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 390/909 (42%) - fn_attachItemWeapons.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 400/909 (44%) - fn_interactDoor.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 410/909 (45%) - fn_interactSelfClicked.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 420/909 (46%) - fn_initHUD.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 430/909 (47%) - mouseDown.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 440/909 (48%) - airdropReq.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 450/909 (49%) - ACmouseDown.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 460/909 (50%) - consoleSwitchMenu.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 470/909 (51%) - groupNumbersSelectionEH.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 480/909 (52%) - UAVmousez.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 490/909 (53%) - b_AAVehicleSiteAmbient.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 500/909 (55%) - b_mortarCampEmpty.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 510/909 (56%) - c_nestBig.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 520/909 (57%) - i_mortarCampEmpty.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 530/909 (58%) - o_mobileArtilleryCampObserver.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 540/909 (59%) - move_heli.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 550/909 (60%) - group_spawnServer.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 560/909 (61%) - jukebox.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 570/909 (62%) - mouseUp.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 580/909 (63%) - um.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 590/909 (64%) - fn_cover.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 600/909 (66%) - fn_spotEnemy.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 610/909 (67%) - fn_calcSolution.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 620/909 (68%) - fn_consoleClickGroupIcon.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 630/909 (69%) - fn_addVelocity.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 640/909 (70%) - fn_gear.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 650/909 (71%) - fn_makeBriefing.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 660/909 (72%) - fn_pickItem.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 670/909 (73%) - fn_saveToSQM.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 680/909 (74%) - fn_time2String.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 690/909 (75%) - fn_createIED.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 700/909 (77%) - fn_SBSingle.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 710/909 (78%) - fn_loadPlayer.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 720/909 (79%) - mcc_sqlpda_rsc_init.sqf
[2025-11-18 13:58:31] [INFO] 正在分析: 730/909 (80%) - fn_moduleCapturePoint.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 740/909 (81%) - fn_addToZeus.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 750/909 (82%) - fn_curatorGarrisonUnits.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 760/909 (83%) - fn_curatorUnderCover.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 770/909 (84%) - fn_bdCreateManual.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 780/909 (85%) - fn_ambientDeleteCiv.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 790/909 (86%) - fn_findCivHouse.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 800/909 (88%) - fn_reinforcement.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 810/909 (89%) - fn_deleteBodies.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 820/909 (90%) - fn_cacheFar.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 830/909 (91%) - fn_addWaypoint.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 840/909 (92%) - fn_generateWaypoints.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 850/909 (93%) - fn_hasLineOfSight.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 860/909 (94%) - fn_getMarkerVertices.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 870/909 (95%) - fn_rotatePosition.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 880/909 (96%) - fn_doAttackMotorizeInfantry.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 890/909 (97%) - fn_doOrganizeTransportation.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 900/909 (99%) - fn_doPatrolShip.sqf
[2025-11-18 13:58:32] [INFO] 正在分析: 909/909 (100%) - openMenu.sqf
[2025-11-18 13:58:32] [INFO] 分析完成，发现 11 个文件需要修复
[2025-11-18 13:58:32] [INFO] 开始修复 11 个文件...
[2025-11-18 13:58:32] [INFO] 修复进度: 1/11 - fn_initCuratorAttribute.sqf
[2025-11-18 13:58:32] [INFO] 添加缺失的闭合括号 } 在行 10
[2025-11-18 13:58:32] [INFO] 添加缺失的闭合括号 } 在行 4
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\UI\fnc\fn_initCuratorAttribute.sqf (2 个问题)
[2025-11-18 13:58:32] [INFO] [试运行] 将修复 addons\mcc_sandbox_mod\mcc\UI\fnc\fn_initCuratorAttribute.sqf
[2025-11-18 13:58:32] [INFO] 修复进度: 2/11 - mcc_logisticsBaseBuild.sqf
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\rts\scripts\mcc_logisticsBaseBuild.sqf (1 个问题)
[2025-11-18 13:58:32] [WARNING] [警告] addons\mcc_sandbox_mod\mcc\rts\scripts\mcc_logisticsBaseBuild.sqf 有括号问题但可能无法自动修复
[2025-11-18 13:58:32] [INFO] 修复进度: 3/11 - fn_MWObjectiveHVT.sqf
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\missionWizard\fnc\fn_MWObjectiveHVT.sqf (1 个问题)
[2025-11-18 13:58:32] [WARNING] [警告] addons\mcc_sandbox_mod\mcc\missionWizard\fnc\fn_MWObjectiveHVT.sqf 有括号问题但可能无法自动修复
[2025-11-18 13:58:32] [INFO] 修复进度: 4/11 - fn_LHDspawnMenuInit.sqf
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\LHD\fnc\fn_LHDspawnMenuInit.sqf (2 个问题)
[2025-11-18 13:58:32] [WARNING] [警告] addons\mcc_sandbox_mod\mcc\LHD\fnc\fn_LHDspawnMenuInit.sqf 有括号问题但可能无法自动修复
[2025-11-18 13:58:32] [INFO] 修复进度: 5/11 - fn_LHDspawnVehicle.sqf
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\LHD\fnc\fn_LHDspawnVehicle.sqf (4 个问题)
[2025-11-18 13:58:32] [WARNING] [警告] addons\mcc_sandbox_mod\mcc\LHD\fnc\fn_LHDspawnVehicle.sqf 有括号问题但可能无法自动修复
[2025-11-18 13:58:32] [INFO] 修复进度: 6/11 - make_convoy_WP.sqf
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\general_scripts\convoy\make_convoy_WP.sqf (1 个问题)
[2025-11-18 13:58:32] [WARNING] [警告] addons\mcc_sandbox_mod\mcc\general_scripts\convoy\make_convoy_WP.sqf 有括号问题但可能无法自动修复
[2025-11-18 13:58:32] [INFO] 修复进度: 7/11 - create_hostage.sqf
[2025-11-18 13:58:32] [INFO] 删除意外的闭合括号 ] 在行 62, 列 1
[2025-11-18 13:58:32] [INFO] 删除意外的闭合括号 ] 在行 40, 列 3
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\general_scripts\hostages\create_hostage.sqf (3 个问题)
[2025-11-18 13:58:32] [INFO] [试运行] 将修复 addons\mcc_sandbox_mod\mcc\general_scripts\hostages\create_hostage.sqf
[2025-11-18 13:58:32] [INFO] 修复进度: 8/11 - fn_keyToName.sqf
[2025-11-18 13:58:32] [INFO] 添加缺失的闭合括号 } 在行 54
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\fnc\general\fn_keyToName.sqf (1 个问题)
[2025-11-18 13:58:32] [INFO] [试运行] 将修复 addons\mcc_sandbox_mod\mcc\fnc\general\fn_keyToName.sqf
[2025-11-18 13:58:32] [INFO] 修复进度: 9/11 - fn_pickItem.sqf
[2025-11-18 13:58:32] [INFO] 添加缺失的闭合括号 } 在行 16
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\fnc\general\fn_pickItem.sqf (1 个问题)
[2025-11-18 13:58:32] [WARNING] [警告] addons\mcc_sandbox_mod\mcc\fnc\general\fn_pickItem.sqf 有括号问题但可能无法自动修复
[2025-11-18 13:58:32] [INFO] 修复进度: 10/11 - fn_bdButtonsModule.sqf
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\bombDefuse\fnc\fn_bdButtonsModule.sqf (2 个问题)
[2025-11-18 13:58:32] [WARNING] [警告] addons\mcc_sandbox_mod\mcc\bombDefuse\fnc\fn_bdButtonsModule.sqf 有括号问题但可能无法自动修复
[2025-11-18 13:58:32] [INFO] 修复进度: 11/11 - fn_ambientFirePlayerFiredEH.sqf
[2025-11-18 13:58:32] [INFO] 删除意外的闭合括号 ] 在行 41, 列 8
[2025-11-18 13:58:32] [INFO] 修复括号问题: addons\mcc_sandbox_mod\mcc\ambient\fnc\fn_ambientFirePlayerFiredEH.sqf (2 个问题)
[2025-11-18 13:58:32] [INFO] [试运行] 将修复 addons\mcc_sandbox_mod\mcc\ambient\fnc\fn_ambientFirePlayerFiredEH.sqf
[2025-11-18 13:58:32] [INFO] ============================================================
[2025-11-18 13:58:32] [INFO] 统计信息:
[2025-11-18 13:58:32] [INFO]   总文件数: 909
[2025-11-18 13:58:32] [INFO]   有问题文件数: 11
[2025-11-18 13:58:32] [INFO]   括号不匹配数: 20
[2025-11-18 13:58:32] [INFO]   重复 if 嵌套数: 0
[2025-11-18 13:58:32] [INFO]   已修复文件数: 4
[2025-11-18 13:58:32] [INFO]   错误数: 0
[2025-11-18 13:58:32] [INFO] ============================================================
```

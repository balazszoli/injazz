import csv

articles = ({'InJazz': '101587', 'EU': 'YA-0020'}, {'InJazz': '101588', 'EU': 'YA-0021'}, {'InJazz': '101589', 'EU': 'YA-0002'},
    {'InJazz': '101599', 'EU': 'YA-0069'}, {'InJazz': '101600', 'EU': 'YA-0068'}, {'InJazz': '101608', 'EU': 'YA-0243'},
    {'InJazz': '101609', 'EU': 'YA-0245'}, {'InJazz': '101610', 'EU': 'YA-0240'}, {'InJazz': '101611', 'EU': 'YA-0241'},
    {'InJazz': '101613', 'EU': 'YA-0242'}, {'InJazz': '101614', 'EU': 'YA-0244'}, {'InJazz': '101616', 'EU': 'YA-0167'},
    {'InJazz': '101618', 'EU': 'YA-0004'}, {'InJazz': '101619', 'EU': 'YA-0139'}, {'InJazz': '101620', 'EU': 'YA-0108'},
    {'InJazz': '101639', 'EU': 'YA-0078'}, {'InJazz': '101661', 'EU': 'YA-0066'}, {'InJazz': '101664', 'EU': 'YA-0043'},
    {'InJazz': '101665', 'EU': 'YA-0045'}, {'InJazz': '101666', 'EU': 'YA-0042'}, {'InJazz': '101676', 'EU': 'YA-0017'},
    {'InJazz': '101678', 'EU': 'YA-0076'}, {'InJazz': '101679', 'EU': 'YA-0285'}, {'InJazz': '101681', 'EU': 'YA-0283'},
    {'InJazz': '101682', 'EU': 'YA-0284'}, {'InJazz': '101687', 'EU': 'YA-0107'}, {'InJazz': '101688', 'EU': 'YA-0259'},
    {'InJazz': '101696', 'EU': 'YA-0261'}, {'InJazz': '101697', 'EU': 'YA-0143'}, {'InJazz': '101700', 'EU': 'YA-0142'},
    {'InJazz': '101705', 'EU': 'YA-0248'}, {'InJazz': '101713', 'EU': 'YA-0249'}, {'InJazz': '101733', 'EU': 'YA-0100'},
    {'InJazz': '101734', 'EU': 'YA-0098'}, {'InJazz': '101735', 'EU': 'YA-0099'}, {'InJazz': '101736', 'EU': 'YA-0097'},
    {'InJazz': '101737', 'EU': 'YA-0096'}, {'InJazz': '101828', 'EU': 'YA-0173'}, {'InJazz': '101831', 'EU': 'YA-0224'},
    {'InJazz': '101832', 'EU': 'YA-0227'}, {'InJazz': '101833', 'EU': 'YA-0225'}, {'InJazz': '101834', 'EU': 'YA-0226'},
    {'InJazz': '101837', 'EU': 'YA-0230'}, {'InJazz': '101838', 'EU': 'YA-0231'}, {'InJazz': '101848', 'EU': 'YA-0074'},
    {'InJazz': '101851', 'EU': 'YA-0075'}, {'InJazz': '101854', 'EU': 'YA-0016'}, {'InJazz': '101860', 'EU': 'YA-0275'},
    {'InJazz': '101861', 'EU': 'YA-0146'}, {'InJazz': '101862', 'EU': 'YA-0147'}, {'InJazz': '101866', 'EU': 'YA-0247'},
    {'InJazz': '101868', 'EU': 'YA-0114'}, {'InJazz': '101869', 'EU': 'YA-0113'}, {'InJazz': '101870', 'EU': 'YA-0116'},
    {'InJazz': '101871', 'EU': 'YA-0115'}, {'InJazz': '101872', 'EU': 'YA-0144'}, {'InJazz': '101876', 'EU': 'YA-0012'},
    {'InJazz': '102015', 'EU': 'TW130ASMOM'}, {'InJazz': '102018', 'EU': 'TW138ASMDCE'}, {'InJazz': '102019', 'EU': 'TW138ASMSD'},
    {'InJazz': '102231', 'EU': 'TCCS'}, {'InJazz': '102930', 'EU': 'EB-0084'}, {'InJazz': '102931', 'EU': 'EB-0052'},
    {'InJazz': '102932', 'EU': 'EB-0060'}, {'InJazz': '102933', 'EU': 'EB-0055'}, {'InJazz': '102946', 'EU': 'EB-0054'},
    {'InJazz': '102954', 'EU': 'EB-0042'}, {'InJazz': '102984', 'EU': 'EB-0047'}, {'InJazz': '102985', 'EU': 'EB-0077'},
    {'InJazz': '102986', 'EU': 'EB-0005'}, {'InJazz': '102990', 'EU': 'EB-0006'}, {'InJazz': '102993', 'EU': 'EB-0015'},
    {'InJazz': '102994', 'EU': 'EB-0023'}, {'InJazz': '102995', 'EU': 'EB-0027'}, {'InJazz': '102996', 'EU': 'EB-0029'},
    {'InJazz': '102997', 'EU': 'EB-0022'}, {'InJazz': '103018', 'EU': 'EB-0028'}, {'InJazz': '103019', 'EU': 'EB-0024'},
    {'InJazz': '103020', 'EU': 'EB-0016'}, {'InJazz': '103021', 'EU': 'EB-0061'}, {'InJazz': '103022', 'EU': 'EB-0048'},
    {'InJazz': '103023', 'EU': 'EB-0078'}, {'InJazz': '104920', 'EU': 'YA-0094'}, {'InJazz': '104921', 'EU': 'YA-0092'},
    {'InJazz': '104922', 'EU': 'YA-0093'}, {'InJazz': '104923', 'EU': 'YA-0095'}, {'InJazz': '104924', 'EU': 'YA-0091'},
    {'InJazz': '104925', 'EU': 'YA-0089'}, {'InJazz': '104926', 'EU': 'YA-0087'}, {'InJazz': '104927', 'EU': 'YA-0090'},
    {'InJazz': '104928', 'EU': 'YA-0088'}, {'InJazz': '104947', 'EU': 'YA-0101'}, {'InJazz': '104957', 'EU': 'YA-0239'},
    {'InJazz': '104959', 'EU': 'YA-0172'}, {'InJazz': '104961', 'EU': 'YA-0168'}, {'InJazz': '105019', 'EU': 'YA-0274'},
    {'InJazz': '105020', 'EU': 'YA-0271'}, {'InJazz': '105021', 'EU': 'YA-0153'}, {'InJazz': '105022', 'EU': 'YA-0086'},
    {'InJazz': '105026', 'EU': 'YA-0035'}, {'InJazz': '105027', 'EU': 'YA-0036'}, {'InJazz': '105028', 'EU': 'YA-0037'},
    {'InJazz': '105037', 'EU': 'YA-0054'}, {'InJazz': '105038', 'EU': 'YA-0140'}, {'InJazz': '105056', 'EU': 'YA-0194'},
    {'InJazz': '105057', 'EU': 'YA-0195'}, {'InJazz': '105058', 'EU': 'YA-0197'}, {'InJazz': '105059', 'EU': 'YA-0200'},
    {'InJazz': '105060', 'EU': 'YA-0129'}, {'InJazz': '105147', 'EU': 'YA-0145'}, {'InJazz': '105150', 'EU': 'YA-0148'},
    {'InJazz': '105169', 'EU': 'YA-0103'}, {'InJazz': '105219', 'EU': 'YA-0202'}, {'InJazz': '105220', 'EU': 'YA-0203'},
    {'InJazz': '105222', 'EU': 'YA-0204'}, {'InJazz': '105223', 'EU': 'YA-0205'}, {'InJazz': '105235', 'EU': 'YA-0196'},
    {'InJazz': '105236', 'EU': 'YA-0199'}, {'InJazz': '105237', 'EU': 'YA-0198'}, {'InJazz': '105302', 'EU': 'YA-0228'},
    {'InJazz': '105305', 'EU': 'YA-0229'}, {'InJazz': '105355', 'EU': 'YA-0201'}, {'InJazz': '106075', 'EU': 'YA-0260'},
    {'InJazz': '106870', 'EU': 'YA-0155'}, {'InJazz': '106871', 'EU': 'YA-0156'}, {'InJazz': '106872', 'EU': 'YA-0157'},
    {'InJazz': '106873', 'EU': 'YA-0159'}, {'InJazz': '106874', 'EU': 'YA-0161'}, {'InJazz': '106875', 'EU': 'YA-0162'},
    {'InJazz': '106876', 'EU': 'YA-0163'}, {'InJazz': '106883', 'EU': 'YA-0186'}, {'InJazz': '106884', 'EU': 'YA-0188'},
    {'InJazz': '106885', 'EU': 'YA-0189'}, {'InJazz': '106888', 'EU': 'YA-0191'}, {'InJazz': '106900', 'EU': 'YA-0001'},
    {'InJazz': '106901', 'EU': 'YA-0003'}, {'InJazz': '106906', 'EU': 'YA-0055'}, {'InJazz': '106907', 'EU': 'YA-0112'},
    {'InJazz': '106908', 'EU': 'YA-0065'}, {'InJazz': '106909', 'EU': 'YA-0267'}, {'InJazz': '106910', 'EU': 'YA-0005'},
    {'InJazz': '106911', 'EU': 'YA-0006'}, {'InJazz': '106914', 'EU': 'YA-0007'}, {'InJazz': '106915', 'EU': 'YA-0084'},
    {'InJazz': '106916', 'EU': 'YA-0085'}, {'InJazz': '106926', 'EU': 'YA-0104'}, {'InJazz': '106927', 'EU': 'YA-0105'},
    {'InJazz': '106928', 'EU': 'YA-0106'}, {'InJazz': '106930', 'EU': 'YA-0123'}, {'InJazz': '107287', 'EU': 'YA-0128'},
    {'InJazz': '107350', 'EU': 'YA-0270'}, {'InJazz': '107351', 'EU': 'YA-0011'}, {'InJazz': '107353', 'EU': 'YA-0013'},
    {'InJazz': '107354', 'EU': 'YA-0014'}, {'InJazz': '107355', 'EU': 'YA-0015'}, {'InJazz': '107356', 'EU': 'YA-0253'},
    {'InJazz': '107358', 'EU': 'YA-0255'}, {'InJazz': '107362', 'EU': 'YA-0254'}, {'InJazz': '107366', 'EU': 'YA-0250'},
    {'InJazz': '107367', 'EU': 'YA-0251'}, {'InJazz': '107368', 'EU': 'YA-0252'}, {'InJazz': '107372', 'EU': 'YA-0273'},
    {'InJazz': '107395', 'EU': 'YA-0151'}, {'InJazz': '107396', 'EU': 'YA-0152'}, {'InJazz': '109770', 'EU': 'ST-0004'},
    {'InJazz': '109772', 'EU': 'ST-0002'}, {'InJazz': '109777', 'EU': 'ST-0003'}, {'InJazz': '109778', 'EU': 'ST-0001'},
    {'InJazz': '109785', 'EU': 'ST-0006'}, {'InJazz': '109790', 'EU': 'ST-0005'}, {'InJazz': '110695', 'EU': 'ST-0011'},
    {'InJazz': '111024', 'EU': 'DBTDLXD'}, {'InJazz': '111025', 'EU': '35619'}, {'InJazz': '113937', 'EU': 'YA-0221'},
    {'InJazz': '113938', 'EU': 'YA-0222'}, {'InJazz': '113939', 'EU': 'YA-0223'}, {'InJazz': '113941', 'EU': 'YA-0217'},
    {'InJazz': '113950', 'EU': 'YA-0218'}, {'InJazz': '113960', 'EU': 'YA-0219'}, {'InJazz': '113963', 'EU': 'YA-0220'},
    {'InJazz': '113994', 'EU': 'YA-0117'}, {'InJazz': '114034', 'EU': 'YA-0031'}, {'InJazz': '114110', 'EU': 'YA-0022'},
    {'InJazz': '114111', 'EU': 'YA-0023'}, {'InJazz': '114113', 'EU': 'YA-0026'}, {'InJazz': '114131', 'EU': 'YA-0024'},
    {'InJazz': '114132', 'EU': 'YA-0025'}, {'InJazz': '114154', 'EU': 'YA-0160'}, {'InJazz': '114156', 'EU': 'YA-0187'},
    {'InJazz': '114161', 'EU': 'YA-0232'}, {'InJazz': '114163', 'EU': 'YA-0233'}, {'InJazz': '114164', 'EU': 'YA-0234'},
    {'InJazz': '114173', 'EU': 'YA-0056'}, {'InJazz': '114178', 'EU': 'YA-0235'}, {'InJazz': '114182', 'EU': 'YA-0238'},
    {'InJazz': '114209', 'EU': 'YA-0077'}, {'InJazz': '114211', 'EU': 'YA-0040'}, {'InJazz': '114212', 'EU': 'YA-0210'},
    {'InJazz': '114213', 'EU': 'YA-0213'}, {'InJazz': '114214', 'EU': 'YA-0237'}, {'InJazz': '114226', 'EU': 'YA-0141'},
    {'InJazz': '114230', 'EU': 'YA-0214'}, {'InJazz': '114231', 'EU': 'YA-0211'}, {'InJazz': '114232', 'EU': 'YA-0212'},
    {'InJazz': '114503', 'EU': 'YA-0053'}, {'InJazz': '114507', 'EU': 'YA-0190'}, {'InJazz': '114586', 'EU': 'YA-0047'},
    {'InJazz': '114592', 'EU': 'YA-0041'}, {'InJazz': '114593', 'EU': 'YA-0044'}, {'InJazz': '114596', 'EU': 'YA-0046'},
    {'InJazz': '114598', 'EU': 'YA-0048'}, {'InJazz': '114601', 'EU': 'YA-0051'}, {'InJazz': '114602', 'EU': 'YA-0052'},
    {'InJazz': '114606', 'EU': 'YA-0049'}, {'InJazz': '114607', 'EU': 'YA-0050'}, {'InJazz': '114620', 'EU': 'YA-0039'},
    {'InJazz': '114621', 'EU': 'YA-0158'}, {'InJazz': '115091', 'EU': 'AM-0035'}, {'InJazz': '115095', 'EU': 'AM-0049'},
    {'InJazz': '115103', 'EU': 'AM-0043'}, {'InJazz': '115104', 'EU': 'AM-0044'}, {'InJazz': '115105', 'EU': 'AM-0045'},
    {'InJazz': '115106', 'EU': 'AM-0046'}, {'InJazz': '115109', 'EU': 'AM-0040'}, {'InJazz': '115110', 'EU': 'AM-0041'},
    {'InJazz': '115114', 'EU': 'AM-0054'}, {'InJazz': '115118', 'EU': 'AM-0042'}, {'InJazz': '115122', 'EU': 'AM-0033'},
    {'InJazz': '115160', 'EU': 'AM-0034'}, {'InJazz': '115162', 'EU': 'AM-0036'}, {'InJazz': '115184', 'EU': 'AM-0037'},
    {'InJazz': '115186', 'EU': 'AM-0039'}, {'InJazz': '115189', 'EU': 'AM-0038'}, {'InJazz': '115221', 'EU': 'AM-0052'},
    {'InJazz': '115222', 'EU': 'AM-0053'}, {'InJazz': '115223', 'EU': 'AM-0055'}, {'InJazz': '115224', 'EU': 'AM-0048'},
    {'InJazz': '115225', 'EU': 'AM-0050'}, {'InJazz': '115226', 'EU': 'AM-0051'}, {'InJazz': '115228', 'EU': 'AM-0047'},
    {'InJazz': '115299', 'EU': 'YA-0072'}, {'InJazz': '115301', 'EU': 'YA-0073'}, {'InJazz': '115336', 'EU': 'YA-0019'},
    {'InJazz': '115344', 'EU': 'YA-0177'}, {'InJazz': '115345', 'EU': 'YA-0176'}, {'InJazz': '115346', 'EU': 'YA-0178'},
    {'InJazz': '115347', 'EU': 'YA-0179'}, {'InJazz': '115348', 'EU': 'YA-0180'}, {'InJazz': '115349', 'EU': 'YA-0181'},
    {'InJazz': '115350', 'EU': 'YA-0118'}, {'InJazz': '115351', 'EU': 'YA-0119'}, {'InJazz': '115352', 'EU': 'YA-0120'},
    {'InJazz': '115353', 'EU': 'YA-0121'}, {'InJazz': '115354', 'EU': 'YA-0122'}, {'InJazz': '115359', 'EU': 'YA-0059'},
    {'InJazz': '115360', 'EU': 'YA-0060'}, {'InJazz': '115361', 'EU': 'YA-0057'}, {'InJazz': '115362', 'EU': 'YA-0058'},
    {'InJazz': '115363', 'EU': 'YA-0132'}, {'InJazz': '115364', 'EU': 'YA-0133'}, {'InJazz': '115365', 'EU': 'YA-0134'},
    {'InJazz': '115366', 'EU': 'YA-0135'}, {'InJazz': '115367', 'EU': 'YA-0137'}, {'InJazz': '115368', 'EU': 'YA-0136'},
    {'InJazz': '115370', 'EU': 'YA-0138'}, {'InJazz': '115379', 'EU': 'YA-0185'}, {'InJazz': '115383', 'EU': 'YA-0064'},
    {'InJazz': '115386', 'EU': 'YA-0067'}, {'InJazz': '115387', 'EU': 'YA-0018'}, {'InJazz': '115414', 'EU': 'YA-0164'},
    {'InJazz': '115420', 'EU': 'YA-0034'}, {'InJazz': '116381', 'EU': 'EB-0001'}, {'InJazz': '116382', 'EU': 'EB-0025'},
    {'InJazz': '116383', 'EU': 'EB-0019'}, {'InJazz': '116384', 'EU': 'EB-0012'}, {'InJazz': '116385', 'EU': 'EB-0017'},
    {'InJazz': '116386', 'EU': 'EB-0010'}, {'InJazz': '116387', 'EU': 'EB-0009'}, {'InJazz': '116388', 'EU': 'EB-0007'},
    {'InJazz': '116389', 'EU': 'EB-0020'}, {'InJazz': '116390', 'EU': 'EB-0013'}, {'InJazz': '116391', 'EU': 'EB-0011'},
    {'InJazz': '116393', 'EU': 'EB-0026'}, {'InJazz': '116394', 'EU': 'EB-0021'}, {'InJazz': '116395', 'EU': 'EB-0014'},
    {'InJazz': '116396', 'EU': 'EB-0018'}, {'InJazz': '116397', 'EU': 'EB-0008'}, {'InJazz': '116398', 'EU': 'EB-0039'},
    {'InJazz': '116399', 'EU': 'EB-0040'}, {'InJazz': '116400', 'EU': 'EB-0041'}, {'InJazz': '116401', 'EU': 'EB-0069'},
    {'InJazz': '116402', 'EU': 'EB-0066'}, {'InJazz': '116403', 'EU': 'EB-0063'}, {'InJazz': '116404', 'EU': 'EB-0050'},
    {'InJazz': '116405', 'EU': 'EB-0051'}, {'InJazz': '116406', 'EU': 'EB-0056'}, {'InJazz': '116407', 'EU': 'EB-0043'},
    {'InJazz': '116408', 'EU': 'EB-0080'}, {'InJazz': '116409', 'EU': 'EB-0073'}, {'InJazz': '116410', 'EU': 'EB-0070'},
    {'InJazz': '116411', 'EU': 'EB-0071'}, {'InJazz': '116412', 'EU': 'EB-0074'}, {'InJazz': '116413', 'EU': 'EB-0044'},
    {'InJazz': '116414', 'EU': 'EB-0081'}, {'InJazz': '116415', 'EU': 'EB-0057'}, {'InJazz': '116416', 'EU': 'EB-0058'},
    {'InJazz': '116417', 'EU': 'EB-0045'}, {'InJazz': '116418', 'EU': 'EB-0082'}, {'InJazz': '116419', 'EU': 'EB-0075'},
    {'InJazz': '116420', 'EU': 'EB-0072'}, {'InJazz': '116421', 'EU': 'EB-0059'}, {'InJazz': '116422', 'EU': 'EB-0046'},
    {'InJazz': '116423', 'EU': 'EB-0083'}, {'InJazz': '116424', 'EU': 'EB-0076'}, {'InJazz': '116434', 'EU': 'EB-0037'},
    {'InJazz': '116435', 'EU': 'EB-0035'}, {'InJazz': '116436', 'EU': 'EB-0033'}, {'InJazz': '116437', 'EU': 'EB-0031'},
    {'InJazz': '116438', 'EU': 'EB-0030'}, {'InJazz': '116439', 'EU': 'EB-0003'}, {'InJazz': '116442', 'EU': 'EB-0036'},
    {'InJazz': '116443', 'EU': 'EB-0034'}, {'InJazz': '116444', 'EU': 'EB-0032'}, {'InJazz': '116468', 'EU': 'EB-0038'},
    {'InJazz': '116477', 'EU': 'EB-0064'}, {'InJazz': '116482', 'EU': 'EB-0067'}, {'InJazz': '116484', 'EU': 'EB-0004'},
    {'InJazz': '116485', 'EU': 'EB-0002'}, {'InJazz': '116494', 'EU': 'EB-0053'}, {'InJazz': '116495', 'EU': 'EB-0062'},
    {'InJazz': '116496', 'EU': 'EB-0049'}, {'InJazz': '116497', 'EU': 'EB-0085'}, {'InJazz': '116498', 'EU': 'EB-0079'},
    {'InJazz': '116500', 'EU': 'EB-0068'}, {'InJazz': '116501', 'EU': 'EB-0065'}, {'InJazz': '117060', 'EU': 'KU-0011'},
    {'InJazz': '117077', 'EU': 'KU-0001'}, {'InJazz': '117803', 'EU': 'ST-0022'}, {'InJazz': '118606', 'EU': 'KU-0007'},
    {'InJazz': '118607', 'EU': 'KU-0008'}, {'InJazz': '118608', 'EU': 'KU-0009'}, {'InJazz': '118609', 'EU': 'KU-0010'},
    {'InJazz': '118611', 'EU': 'KU-0016'}, {'InJazz': '118612', 'EU': 'KU-0014'}, {'InJazz': '118613', 'EU': 'KU-0015'},
    {'InJazz': '118614', 'EU': 'KU-0017'}, {'InJazz': '118615', 'EU': 'KU-0002'}, {'InJazz': '118616', 'EU': 'KU-0012'},
    {'InJazz': '118617', 'EU': 'KU-0013'}, {'InJazz': '118622', 'EU': 'KU-0006'}, {'InJazz': '118623', 'EU': 'KU-0003'},
    {'InJazz': '118624', 'EU': 'KU-0004'}, {'InJazz': '118625', 'EU': 'KU-0005'}, {'InJazz': '121433', 'EU': 'YA-0193'},
    {'InJazz': '121553', 'EU': 'YA-0079'}, {'InJazz': '121554', 'EU': 'YA-0080'}, {'InJazz': '121556', 'EU': 'YA-0032'},
    {'InJazz': '121557', 'EU': 'YA-0033'}, {'InJazz': '121665', 'EU': 'YA-0165'}, {'InJazz': '121666', 'EU': 'YA-0166'},
    {'InJazz': '121676', 'EU': 'YA-0192'}, {'InJazz': '121690', 'EU': 'YA-0125'}, {'InJazz': '121730', 'EU': 'YA-0102'},
    {'InJazz': '121732', 'EU': 'YA-0038'}, {'InJazz': '121739', 'EU': 'YA-0209'}, {'InJazz': '121740', 'EU': 'YA-0206'},
    {'InJazz': '121741', 'EU': 'YA-0207'}, {'InJazz': '121742', 'EU': 'YA-0208'}, {'InJazz': '121743', 'EU': 'YA-0061'},
    {'InJazz': '121744', 'EU': 'YA-0062'}, {'InJazz': '121746', 'EU': 'YA-0182'}, {'InJazz': '121747', 'EU': 'YA-0183'},
    {'InJazz': '121748', 'EU': 'YA-0184'}, {'InJazz': '121749', 'EU': 'YA-0169'}, {'InJazz': '121752', 'EU': 'YA-0063'},
    {'InJazz': '121808', 'EU': 'YA-0127'}, {'InJazz': '121865', 'EU': 'YA-0174'}, {'InJazz': '121866', 'EU': 'YA-0264'},
    {'InJazz': '121867', 'EU': 'YA-0175'}, {'InJazz': '121892', 'EU': 'YA-0009'}, {'InJazz': '121999', 'EU': 'YA-0236'},
    {'InJazz': '122011', 'EU': 'YA-0109'}, {'InJazz': '122013', 'EU': 'YA-0110'}, {'InJazz': '122014', 'EU': 'YA-0111'},
    {'InJazz': '122020', 'EU': 'YA-0124'}, {'InJazz': '122026', 'EU': 'YA-0126'}, {'InJazz': '123075', 'EU': 'ST-0012'},
    {'InJazz': '123627', 'EU': 'YA-0246'}, {'InJazz': '123628', 'EU': 'YA-0027'}, {'InJazz': '123629', 'EU': 'YA-0028'},
    {'InJazz': '123630', 'EU': 'YA-0029'}, {'InJazz': '123631', 'EU': 'YA-0030'}, {'InJazz': '123632', 'EU': 'YA-0256'},
    {'InJazz': '123633', 'EU': 'YA-0257'}, {'InJazz': '123634', 'EU': 'YA-0258'}, {'InJazz': '123646', 'EU': 'YA-0281'},
    {'InJazz': '123647', 'EU': 'YA-0170'}, {'InJazz': '123648', 'EU': 'YA-0171'}, {'InJazz': '123807', 'EU': 'YA-0149'},
    {'InJazz': '123808', 'EU': 'YA-0150'}, {'InJazz': '124046', 'EU': 'YA-0282'}, {'InJazz': '125195', 'EU': 'YA-0286'}
)

# connect to ftp, download NEW.csv
# ftp://91.235.69.81:21
# User: user45
# Pass: Ftp+us-45+pass
# CSV  - NEW.csv

def search(name):
    for p in articles:
        if p['InJazz'] == name:
            return p['EU']
            break

with open('NEW.csv', encoding='utf-8') as csv_file:  # file from Injazz with data to change for import
    csv_reader = csv.reader(csv_file, delimiter=';')
    data = list(csv_reader)
    list_length = len(data)
print('Progress: |', end="")
step = list_length/50
ungebung = 2*list_length/10000000
with open('NEW.csv', encoding='utf-8') as csv_file:  # file from Injazz with data to change for import
    csv_reader = csv.reader(csv_file, delimiter=';')
    with open("injazz2import.csv", "w", encoding='utf-8', newline='') as import_file:
        fieldnames = ['Артикул', 'Цена', 'Наличие']
        writer = csv.DictWriter(import_file, fieldnames=fieldnames, delimiter=',')

        writer.writeheader()
        # row[5] - price, row[1] - article. if article or price is empty - skip, is price lower than 3 - skip
        rows = 0
        for row in csv_reader:
            if (row[1] != '') and (row[5] != '') and (float(row[5].replace(',', '.')) > 3.0):
                art_value = row[1]  # change to inline list, instead of file reading
                # with open('article-injazz.csv', 'r') as arts_file:  # articles to change, if we have other articles
                #     arts = csv.DictReader(arts_file, delimiter=';')
                for roww in articles:
                    if art_value == roww['InJazz']:
                        art_value = roww['EU']
#                art_value = search(art_value)
#                art_value = next((item.get('EU') for item in articles if item['InJazz'] == row[1]), art_value)
                # change stock statuses
                if row[4] == "есть":
                    inStock = "В наличии"
                elif row[4] == "нет":
                    inStock = "Нет в наличии"
                else:
                    inStock = "Ожидается"
                writer.writerow({'Артикул': art_value, 'Цена': row[5], 'Наличие': inStock})  # 'Поставщик' : 'Ін-Джаз'
            rows = rows + 1
            if abs(int(rows/step)-rows/step) < ungebung:
                print(f'█', end="")
    print('| - Complete!')
    print("File for importing to Horoshop is ready!")

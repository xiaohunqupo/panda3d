from PandaObject import *
from ClusterClient import *
import string

# A dictionary of information for various cluster configurations.
# Dictionary is keyed on cluster-config string
# Each dictionary contains a list of display configurations, one for
# each display in the cluster
# Information that can be specified for each display:
#      display name: Name of display (used in Configrc to specify server)
#      display type: Used to flag client vs. server
#      pos:   positional offset of display's camera from main cluster group
#      hpr:   orientation offset of display's camera from main cluster group
#      focal length: display's focal length (in mm)
#      film size: display's film size (in inches)
#      film offset: offset of film back (in inches)
# Note: Note, this overrides offsets specified in DirectCamConfig.py
# For now we only specify frustum for first display region of configuration
# TODO: Need to handle multiple display regions per cluster node and to
# generalize to non cluster situations

ClientConfigs = {
    'single-server'       : [{'display name' : 'display0',
                              'display mode' : 'client',
                              'pos' : Vec3(0),
                              'hpr' : Vec3(0)}
                             ],
    'two-server'          : [{'display name' : 'master',
                              'display mode' : 'client',
                              'pos' : Vec3(0),
                              'hpr' : Vec3(30,0,0)},
                             {'display name' : 'la',
                              'pos' : Vec3(0),
                              'hpr' : Vec3(-30,0,0)}
                             ],
    'mono-cave'   : [{'display name' : 'la',
                      'pos' : Vec3(-0.105, -0.020, 5.000),
                      'hpr' : Vec3(51.213, 0.000, 0.000),
                      'focal length' : 0.809,
                      'film size' : (1.000, 0.831),
                      'film offset' : (0.000, 0.173),
                      },
                     {'display name' : 'lb',
                      'display mode' : 'client',
                      'pos' : Vec3(-0.105, -0.020, 5.000),
                      'hpr' : Vec3(-0.370, 0.000, 0.000),
                      'focal length' : 0.815,
                      'film size' : (1.000, 0.831),
                      'film offset' : (0.000, 0.173),
                      },
                     {'display name' : 'lc',
                      'pos' : Vec3(-0.105, -0.020, 5.000),
                      'hpr' : Vec3(-51.675, 0.000, 0.000),
                      'focal length' : 0.820,
                      'film size' : (1.000, 0.830),
                      'film offset' : (-0.000, 0.173),
                      },
                     ],
    'seamless-cave'   : [{'display name' : 'master',
                          'display mode' : 'client',
                          'pos' : Vec3(-0.105, -0.020, 5.000),
                          'hpr' : Vec3(-0.370, 0.000, 0.000),
                          'focal length' : 0.815,
                          'film size' : (1.000, 0.831),
                          'film offset' : (0.000, 0.173),
                          },
                         {'display name' : 'la',
                          'pos' : Vec3(-0.105, -0.020, 5.000),
                          'hpr' : Vec3(51.213, 0.000, 0.000),
                          'focal length' : 0.809,
                          'film size' : (1.000, 0.831),
                          'film offset' : (0.000, 0.173),
                          },
                         {'display name' : 'lb',
                          'pos' : Vec3(-0.105, -0.020, 5.000),
                          'hpr' : Vec3(-0.370, 0.000, 0.000),
                          'focal length' : 0.815,
                          'film size' : (1.000, 0.831),
                          'film offset' : (0.000, 0.173),
                          },
                         {'display name' : 'lc',
                          'pos' : Vec3(-0.105, -0.020, 5.000),
                          'hpr' : Vec3(-51.675, 0.000, 0.000),
                          'focal length' : 0.820,
                          'film size' : (1.000, 0.830),
                          'film offset' : (-0.000, 0.173),
                          },
                         {'display name' : 'ra',
                          'pos' : Vec3(0.105, -0.020, 5.000),
                          'hpr' : Vec3(51.675, 0.000, 0.000),
                          'focal length' : 0.820,
                          'film size' : (1.000, 0.830),
                          'film offset' : (0.000, 0.173),
                          },
                         {'display name' : 'rb',
                          'pos' : Vec3(0.105, -0.020, 5.000),
                          'hpr' : Vec3(0.370, 0.000, 0.000),
                          'focal length' : 0.815,
                          'film size' : (1.000, 0.831),
                          'film offset' : (0.000, 0.173),
                          },
                         {'display name' : 'rc',
                          'pos' : Vec3(0.105, -0.020, 5.000),
                          'hpr' : Vec3(-51.213, 0.000, 0.000),
                          'focal length' : 0.809,
                          'film size' : (1.000, 0.831),
                          'film offset' : (-0.000, 0.173),
                          },
                         ],
    'nemo-cave'        : [{'display name' : 'master',
                           'display mode' : 'client',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(-0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'la',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(51.213, 0.000, 0.000),
                           'focal length' : 0.809,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'lb',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(-0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'lc',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(-51.675, 0.000, 0.000),
                           'focal length' : 0.820,
                           'film size' : (1.000, 0.830),
                           'film offset' : (-0.000, 0.173),
                           },
                          {'display name' : 'ra',
                           'pos' : Vec3(0.105, -0.020, 5.000),
                           'hpr' : Vec3(51.675, 0.000, 0.000),
                           'focal length' : 0.820,
                           'film size' : (1.000, 0.830),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rb',
                           'pos' : Vec3(0.105, -0.020, 5.000),
                           'hpr' : Vec3(0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rc',
                           'pos' : Vec3(0.105, -0.020, 5.000),
                           'hpr' : Vec3(-51.213, 0.000, 0.000),
                           'focal length' : 0.809,
                           'film size' : (1.000, 0.831),
                           'film offset' : (-0.000, 0.173),
                           },
                          {'display name' : 'lAudienceL',
                           'pos' : Vec3(-4.895, -0.020, 5.000),
                           'hpr' : Vec3(51.213, 0.000, 0.000),
                           'focal length' : 0.809,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rAudienceL',
                           'pos' : Vec3(-5.105, -8.0, 5.000),
                           'hpr' : Vec3(51.675, 0.000, 0.000),
                           'focal length' : 0.820,
                           'film size' : (1.000, 0.830),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'lAudienceR',
                           'pos' : Vec3(5.105, -0.020, 5.000),
                           'hpr' : Vec3(-51.213, 0.000, 0.000),
                           'focal length' : 0.809,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rAudienceR',
                           'pos' : Vec3(4.895, -8.0, 5.000),
                           'hpr' : Vec3(-51.675, 0.000, 0.000),
                           'focal length' : 0.820,
                           'film size' : (1.000, 0.830),
                           'film offset' : (0.000, 0.173),
                           },
                          ],
    'nemo-cave-narrow' : [{'display name' : 'master',
                           'display mode' : 'client',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(-0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'la',
                           'pos' : Vec3(-0.105, -19.890, 5.000),
                           'hpr' : Vec3(51.500, 0.000, 0.000),
                           'focal length' : 1.662,
                           'film size' : (1.000, 0.828),
                           'film offset' : (1.079, 0.173),
                           },
                          {'display name' : 'lb',
                           'pos' : Vec3(-0.105, -19.890, 5.000),
                           'hpr' : Vec3(0.000, 0.000, 0.000),
                           'focal length' : 2.186,
                           'film size' : (1.000, 0.828),
                           'film offset' : (0.007, 0.173),
                           },
                          {'display name' : 'lc',
                           'pos' : Vec3(-0.105, -19.890, 5.000),
                           'hpr' : Vec3(-51.500, 0.000, 0.000),
                           'focal length' : 1.673,
                           'film size' : (1.000, 0.828),
                           'film offset' : (-1.070, 0.173),
                           },
                          {'display name' : 'ra',
                           'pos' : Vec3(0.105, -19.890, 5.000),
                           'hpr' : Vec3(51.500, 0.000, 0.000),
                           'focal length' : 1.673,
                           'film size' : (1.000, 0.828),
                           'film offset' : (1.070, 0.173),
                           },
                          {'display name' : 'rb',
                           'pos' : Vec3(0.105, -19.890, 5.000),
                           'hpr' : Vec3(0.000, 0.000, 0.000),
                           'focal length' : 2.186,
                           'film size' : (1.000, 0.828),
                           'film offset' : (-0.007, 0.173),
                           },
                          {'display name' : 'rc',
                           'pos' : Vec3(0.105, -19.890, 5.000),
                           'hpr' : Vec3(-51.500, 0.000, 0.000),
                           'focal length' : 1.662,
                           'film size' : (1.000, 0.828),
                           'film offset' : (-1.079, 0.173),
                           },
                          {'display name' : 'lAudienceL',
                           'pos' : Vec3(-0.105, -19.890, 5.000),
                           'hpr' : Vec3(55.706, 0.000, 0.000),
                           'focal length' : 1.225,
                           'film size' : (1.000, 0.762),
                           'film offset' : (-0.195, 0.095),
                           },
                          {'display name' : 'rAudienceL',
                           'pos' : Vec3(0.105, -19.890, 5.000),
                           'hpr' : Vec3(55.706, 0.000, 0.000),
                           'focal length' : 1.241,
                           'film size' : (1.000, 0.762),
                           'film offset' : (-0.206, 0.095),
                           },
                          {'display name' : 'lAudienceR',
                           'pos' : Vec3(-0.105, -19.890, 5.000),
                           'hpr' : Vec3(-62.162, 0.000, 0.000),
                           'focal length' : 1.554,
                           'film size' : (1.000, 0.801),
                           'film offset' : (-0.026, 0.100),
                           },
                          {'display name' : 'rAudienceR',
                           'pos' : Vec3(0.105, -19.890, 5.000),
                           'hpr' : Vec3(-62.162, 0.000, 0.000),
                           'focal length' : 1.536,
                           'film size' : (1.000, 0.801),
                           'film offset' : (-0.036, 0.100),
                           },
                          {'display name' : 'lCart',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(-0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rCart',
                           'pos' : Vec3(0.105, -0.020, 5.000),
                           'hpr' : Vec3(0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          ],
    'fourd-cave'        : [{'display name' : 'master',
                            'display mode' : 'client',
                            'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(-0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'la',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(51.213, 0.000, 0.000),
                           'focal length' : 0.809,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'lb',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(-0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'lc',
                           'pos' : Vec3(-0.105, -0.020, 5.000),
                           'hpr' : Vec3(-51.675, 0.000, 0.000),
                           'focal length' : 0.820,
                           'film size' : (1.000, 0.830),
                           'film offset' : (-0.000, 0.173),
                           },
                          {'display name' : 'ra',
                           'pos' : Vec3(0.105, -0.020, 5.000),
                           'hpr' : Vec3(51.675, 0.000, 0.000),
                           'focal length' : 0.820,
                           'film size' : (1.000, 0.830),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rb',
                           'pos' : Vec3(0.105, -0.020, 5.000),
                           'hpr' : Vec3(0.370, 0.000, 0.000),
                           'focal length' : 0.815,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rc',
                           'pos' : Vec3(0.105, -0.020, 5.000),
                           'hpr' : Vec3(-51.213, 0.000, 0.000),
                           'focal length' : 0.809,
                           'film size' : (1.000, 0.831),
                           'film offset' : (-0.000, 0.173),
                           },
                          {'display name' : 'lAudienceL',
                           'pos' : Vec3(-4.895, -0.020, 5.000),
                           'hpr' : Vec3(65.213, 0.000, 0.000),
                           'focal length' : 0.809,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rAudienceL',
                           'pos' : Vec3(-5.105, -8.0, 5.000),
                           'hpr' : Vec3(65.675, 0.000, 0.000),
                           'focal length' : 0.820,
                           'film size' : (1.000, 0.830),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'lAudienceR',
                           'pos' : Vec3(5.105, -0.020, 5.000),
                           'hpr' : Vec3(-65.213, 0.000, 0.000),
                           'focal length' : 0.809,
                           'film size' : (1.000, 0.831),
                           'film offset' : (0.000, 0.173),
                           },
                          {'display name' : 'rAudienceR',
                           'pos' : Vec3(4.895, -8.0, 5.000),
                           'hpr' : Vec3(-65.675, 0.000, 0.000),
                           'focal length' : 0.820,
                           'film size' : (1.000, 0.830),
                           'film offset' : (0.000, 0.173),
                           },
                          ],
    'parallax-cave'        : [{'display name' : 'master',
                              'display mode' : 'client',
                              'pos': Vec3(0),
                              'hpr': Vec3(0),
                              'focal length' : 0.815,
                              'film size' : (1.000, 0.831),
                              'film offset' : (0.000, 0.173),
                              },
                             {'display name' : 'la',
                              'pos': Vec3(0),
                              'hpr': Vec3(0),
                              'focal length' : 0.809,
                              'film size' : (1.000, 0.831),
                              'film offset' : (0.000, 0.173),
                              },
                             {'display name' : 'lb',
                              'pos': Vec3(0),
                              'hpr': Vec3(0),
                              'focal length' : 0.815,
                              'film size' : (1.000, 0.831),
                              'film offset' : (0.000, 0.173),
                              },
                             {'display name' : 'lc',
                              'pos': Vec3(0),
                              'hpr': Vec3(0),
                              'focal length' : 0.820,
                              'film size' : (1.000, 0.830),
                              'film offset' : (-0.000, 0.173),
                              },
                             {'display name' : 'ra',
                              'pos': Vec3(0),
                              'hpr': Vec3(0),
                              'focal length' : 0.820,
                              'film size' : (1.000, 0.830),
                              'film offset' : (0.000, 0.173),
                              },
                             {'display name' : 'rb',
                              'pos': Vec3(0),
                              'hpr': Vec3(0),
                              'focal length' : 0.815,
                              'film size' : (1.000, 0.831),
                              'film offset' : (0.000, 0.173),
                              },
                             {'display name' : 'rc',
                              'pos': Vec3(0),
                              'hpr': Vec3(0),
                              'focal length' : 0.809,
                              'film size' : (1.000, 0.831),
                              'film offset' : (-0.000, 0.173),
                              },
                             ],
    'carttest'            : [{'display name' : 'master',
                              'display mode' : 'client',
                              'pos' : Vec3(0),
                              'hpr' : Vec3(0),
                              },
                             {'display name' : 'left',
                              'pos' : Vec3(-.105,0,0),
                              'hpr' : Vec3(0,0,-90)},
                             {'display name' : 'right',
                              'pos' : Vec3(.105,0,0),
                              'hpr' : Vec3(0,0,-90)}
                             ],
    }


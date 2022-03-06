max_temp_stats = [
    {
        '$group': {
            '_id': {
                'city': '$city', 
                'month': '$month'
            }, 
            'count': {
                '$sum': 1
            }, 
            'max_temp': {
                '$max': {
                    '$max': '$current.temp'
                }
            }, 
            'docs': {
                '$push': '$$ROOT'
            }
        }
    }, {
        '$addFields': {
            'max_temp_collection': {
                '$filter': {
                    'input': '$docs', 
                    'as': 'doc', 
                    'cond': {
                        '$eq': [
                            '$max_temp', '$$doc.current.temp'
                        ]
                    }
                }
            }
        }
    }, {
        '$unwind': {
            'path': '$max_temp_collection'
        }
    }, {
        '$project': {
            'docs': 0, 
            'count': 0
        }
    }
]


get_stats = [
    {
        '$group': {
            '_id': '$current.dt', 
            'max_temp': {
                '$max': {
                    '$max': '$current.temp'
                }
            }, 
            'min_temp': {
                '$min': {
                    '$min': '$current.temp'
                }
            }, 
            'avg_temp': {
                '$avg': {
                    '$avg': '$current.temp'
                }
            }, 
            'docs': {
                '$push': '$$ROOT'
            }
        }
    }, {
        '$addFields': {
            'max_temp_collection': {
                '$filter': {
                    'input': '$docs', 
                    'as': 'doc', 
                    'cond': {
                        '$eq': [
                            '$max_temp', '$$doc.current.temp'
                        ]
                    }
                }
            }, 
            'min_temp_collection': {
                '$filter': {
                    'input': '$docs', 
                    'as': 'doc', 
                    'cond': {
                        '$eq': [
                            '$min_temp', '$$doc.current.temp'
                        ]
                    }
                }
            }
        }
    }, {
        '$unwind': {
            'path': '$max_temp_collection'
        }
    }, {
        '$unwind': {
            'path': '$min_temp_collection'
        }
    }, {
        '$project': {
            'docs': 0
        }
    }
]
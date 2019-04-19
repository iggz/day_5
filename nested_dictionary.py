
digitalcrafts = {
    'US': { 
        'Georgia': {
            'Atlanta': '3423 Piedmont Rd NE #415',
        },
        'Texas': {
            'Houston': '3302 Canal St.'
        }
    }
}

# Add a new campus

digitalcrafts['US']['Florida'] = {
    'Orlando': 'Communicore Epcot'
}

# Add a new campus to uk
digitalcrafts['UK'] = {
    'Surrey': {
    'London': 'wherever'
    }
}


print(digitalcrafts)
# print(digitalcrafts['US']['Georgia']['Atlanta'])
# print(digitalcrafts['US']['Georgia'])
# print(digitalcrafts['US'])

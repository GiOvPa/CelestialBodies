from rdflib import Graph, Literal, URIRef

g = Graph()
g.parse("../Dataset_rdf_final.ttl")

def meteorite_names():
    res = []
    name_meteorite = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?name
    WHERE {
        ?idMeteo a cbo:Meteorite ;
            cbo:hasName ?name ;
    }
    """)
    for row in name_meteorite:
        res.append(row.name.toPython())
    return res

def meteorite_by_year(nome_r, intorno):
    res = []
    max = nome_r + intorno
    min = nome_r - intorno
    meteorite = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?name
    WHERE {
        ?meteorite a cbo:Meteorite ;
            cbo:hasName ?name ;
            cbo:year ?year ;
        OPTIONAL { ?meteorite owl:sameAs ?dbpedia }

            FILTER (?year >= ?min && ?year <= ?max)
    }
    """,initBindings={'max': Literal(max), 'min': Literal(min)})
    for row in meteorite:
        res.append(row.name.toPython())
    return res

def meteorite_by_type(nome_r):
    res = []
    meteorite = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?fall ?name ?id ?mass ?nametype ?type ?year ?geo ?lat ?long ?dbpedia
    WHERE {
        ?meteorite a cbo:Meteorite ;
            cbo:hasName ?name ;
            cbo:type ?type ;
        OPTIONAL { ?meteorite owl:sameAs ?dbpedia }

            FILTER (?type = ?nome_r)
    }
    """,initBindings={'nome_r': Literal(nome_r)})

    for row in meteorite:
        res.append(row.name.toPython())
    return res

def meteorite_ids():
    res = []
    id_meteorite = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?id
    WHERE {
        ?idMeteo a cbo:Meteorite ;
            cbo:hasId ?id ;
    }
    """)
    for row in id_meteorite:
        res.append(row.id.toPython())
    return res

def meteorite_all(nome_r):
    res = []
    meteorite = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?fall ?name ?id ?mass ?nametype ?type ?year ?geo ?lat ?long ?dbpedia
    WHERE {
        ?meteorite a cbo:Meteorite ;
            cbo:fall ?fall ;
            cbo:hasName ?name ;
            cbo:hasId ?id ;
            cbo:hasMass ?mass ;
            cbo:hasNameType ?nametype ;
            cbo:type ?type ;
            cbo:year ?year ;
            cbo:hasGeographicPosition ?geo ;
            cbo:hasLatitude ?lat ;
            cbo:hasLongitude ?long ;
        OPTIONAL { ?meteorite owl:sameAs ?dbpedia }

            FILTER (?name = ?nome_r)
    }
    """,initBindings={'nome_r': Literal(nome_r)})

    for row in meteorite:
        res.append({
            'fall' : row.fall,
            'name' : row.name,
            'mass' : row.mass,
            'id' : row.id,
            'nametype' : row.nametype,
            'type' : row.type,
            'year' : row.year,
            'dbpedia' : row.dbpedia,
            'geo' : row.geo,
            'lat' : row.lat,
            'long' : row.long
        })
    return res

def meteorite_by_id(nome_r):
    uri = URIRef('http://www.celestial.bodies.org/resource/'+nome_r)
    res = []
    meteorite = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?fall ?name ?id ?mass ?nametype ?type ?year ?geo ?lat ?long ?dbpedia
    WHERE {
        ?meteorite a cbo:Meteorite ;
            cbo:fall ?fall ;
            cbo:hasName ?name ;
            cbo:hasId ?id ;
            cbo:hasMass ?mass ;
            cbo:hasNameType ?nametype ;
            cbo:type ?type ;
            cbo:year ?year ;
            cbo:hasGeographicPosition ?geo ;
            cbo:hasLatitude ?lat ;
            cbo:hasLongitude ?long ;
        OPTIONAL { ?meteorite owl:sameAs ?dbpedia }

    }
    """,initBindings={'meteorite': URIRef(uri)})

    for row in meteorite:
        res.append({
            'fall' : row.fall,
            'name' : row.name,
            'mass' : row.mass,
            'id' : row.id,
            'nametype' : row.nametype,
            'type' : row.type,
            'year' : row.year,
            'dbpedia' : row.dbpedia,
            'geo' : row.geo,
            'lat' : row.lat,
            'long' : row.long
        })
    return res

def comet_names():
    res = []
    nome_cometa = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?nome
    WHERE {
        ?idCometa a cbo:Comet ;
            cbo:hasFullName ?nome ;
    }
    """)
    for row in nome_cometa:
        res.append(row.nome.toPython())
    return res

def comet_ids():
    res = []
    id_cometa = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?id
    WHERE {
        ?idCometa a cbo:Comet ;
            cbo:hasId ?id ;
    }
    """)
    for row in id_cometa:
        res.append(row.id.toPython())
    return res

def asteroid_names():
    res = []
    nome_asteroide = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?nome
    WHERE {
        ?idAsteroide a cbo:Asteroid ;
            cbo:hasFullName ?nome ;
    }
    """)
    for row in nome_asteroide:
        res.append(row.nome.toPython())
    return res

def search_orb_by_name(nome):
    res = []
    orbit = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?orb
    WHERE {
        ?body a ?celestialbody ;
            cbo:hasFullName ?fullname ;
            cbo:hasOrbit ?orb
        FILTER (?fullname = ?nome)
    }
    """,initBindings={'nome': Literal(nome)}
    )
    for row in orbit:
        fullname = row.orb.toPython()
        fullname = fullname.split("/")[-1]
        res.append(fullname)
    return res

def asteroid_ids():
    res = []
    id_asteroide = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?id
    WHERE {
        ?idAsteroide a cbo:Asteroid ;
            cbo:hasId ?id ;
    }
    """)
    for row in id_asteroide:
        res.append(row.id.toPython())
    return res

def orbit_ids():
    res = []
    orbit_id = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?id
    WHERE {
        ?id a cbo:Orbit ;
    }
    """)
    for row in orbit_id:
        uri = row.id.toPython()
        orbit_num = uri.split("/")[-1]
        res.append(orbit_num)
    return res

def comet_by_name(nome_r):
    res = []
    comet = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?primobs ?fullname ?id ?name ?obs ?orbit ?pdes ?lastobs ?dbpedia 
    WHERE {
        ?comet a cbo:Comet ;
            cbo:firstObservation ?primobs ;
            cbo:hasFullName ?fullname ;
            cbo:hasId ?id ;
            cbo:hasName ?name ;
            cbo:hasOberservations ?obs ;
            cbo:hasOrbit ?orbit ;
            cbo:hasPrimaryDesignation ?pdes ;
            cbo:lastObservation ?lastobs ;
        OPTIONAL { ?comet owl:sameAs ?dbpedia }

            FILTER (?name = ?nome_r)
    }
    """,initBindings={'nome_r': Literal(nome_r)})

    for row in comet:
        res.append({
            'name' : row.name,
            'fullname' : row.fullname,
            'orbit' : row.orbit,
            'id' : row.id,
            'primobs' : row.primobs,
            'lastobs' : row.lastobs,
            'pdes' : row.pdes,
            'dbpedia' : row.dbpedia,
            'obs' : row.obs
        })
    return res

def comet_all(nome_r):
    res = []
    comet = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?primobs ?fullname ?id ?name ?obs ?orbit ?pdes ?lastobs ?dbpedia 
    WHERE {
        ?comet a cbo:Comet ;
            cbo:firstObservation ?primobs ;
            cbo:hasFullName ?fullname ;
            cbo:hasId ?id ;
            cbo:hasName ?name ;
            cbo:hasOberservations ?obs ;
            cbo:hasOrbit ?orbit ;
            cbo:hasPrimaryDesignation ?pdes ;
            cbo:lastObservation ?lastobs ;
        OPTIONAL { ?comet owl:sameAs ?dbpedia }

            FILTER (?fullname = ?nome_r)
    }
    """,initBindings={'nome_r': Literal(nome_r)})

    for row in comet:
        res.append({
            'name' : row.name,
            'fullname' : row.fullname,
            'orbit' : row.orbit,
            'id' : row.id,
            'primobs' : row.primobs,
            'lastobs' : row.lastobs,
            'pdes' : row.pdes,
            'dbpedia' : row.dbpedia,
            'obs' : row.obs
        })
    return res

def asteroid_all(nome_r):
    res = []
    asteroid = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?primobs ?fullname ?id ?name ?obs ?orbit ?pdes ?lastobs ?dbpedia 
    WHERE {
        ?asteroid a cbo:Asteroid ;
            cbo:firstObservation ?primobs ;
            cbo:hasFullName ?fullname ;
            cbo:hasId ?id ;
            cbo:hasOberservations ?obs ;
            cbo:hasOrbit ?orbit ;
            cbo:hasPrimaryDesignation ?pdes ;
            cbo:lastObservation ?lastobs ;
        OPTIONAL{ ?asteroid owl:sameAs ?dbpedia  } 
        OPTIONAL{ ?asteroid cbo:hasName ?name }

            FILTER (?fullname = ?nome_r)
    }
    """,initBindings={'nome_r': Literal(nome_r)})

    for row in asteroid:
        res.append({
            'name' : row.name,
            'fullname' : row.fullname,
            'orbit' : row.orbit,
            'id' : row.id,
            'primobs' : row.primobs,
            'lastobs' : row.lastobs,
            'pdes' : row.pdes,
            'dbpedia' : row.dbpedia,
            'obs' : row.obs
        })
    return res

def asteroid_by_id(nome_r):
    uri = URIRef('http://www.celestial.bodies.org/resource/'+nome_r)
    res = []
    asteroid = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?primobs ?fullname ?id ?name ?obs ?orbit ?pdes ?lastobs ?dbpedia 
    WHERE {
        ?asteroide a cbo:Asteroid ;
            cbo:firstObservation ?primobs ;
            cbo:hasFullName ?fullname ;
            cbo:hasId ?id ;
            cbo:hasName ?name ;
            cbo:hasOberservations ?obs ;
            cbo:hasOrbit ?orbit ;
            cbo:hasPrimaryDesignation ?pdes ;
            cbo:lastObservation ?lastobs ;
        OPTIONAL { ?asteroide owl:sameAs ?dbpedia }

    }
    """,initBindings={'asteroide': URIRef(uri)})

    for row in asteroid:
        res.append({
            'name' : row.name,
            'fullname' : row.fullname,
            'orbit' : row.orbit,
            'id' : row.id,
            'primobs' : row.primobs,
            'lastobs' : row.lastobs,
            'pdes' : row.pdes,
            'dbpedia' : row.dbpedia,
            'obs' : row.obs
        })
    return res


def comet_by_id(nome_r):
    uri = URIRef('http://www.celestial.bodies.org/resource/'+nome_r)
    res = []
    comet = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?primobs ?fullname ?id ?name ?obs ?orbit ?pdes ?lastobs ?dbpedia 
    WHERE {
        ?cometa a cbo:Comet ;
            cbo:firstObservation ?primobs ;
            cbo:hasFullName ?fullname ;
            cbo:hasId ?id ;
            cbo:hasName ?name ;
            cbo:hasOberservations ?obs ;
            cbo:hasOrbit ?orbit ;
            cbo:hasPrimaryDesignation ?pdes ;
            cbo:lastObservation ?lastobs ;
        OPTIONAL { ?cometa owl:sameAs ?dbpedia }

    }
    """,initBindings={'cometa': URIRef(uri)})

    for row in comet:
        res.append({
            'name' : row.name,
            'fullname' : row.fullname,
            'orbit' : row.orbit,
            'id' : row.id,
            'primobs' : row.primobs,
            'lastobs' : row.lastobs,
            'pdes' : row.pdes,
            'dbpedia' : row.dbpedia,
            'obs' : row.obs
        })
    return res

def comet_by_uri(uri):
    res = []
    comet = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?primobs ?fullname ?id ?name ?obs ?orbit ?pdes ?lastobs ?dbpedia 
    WHERE {
        ?cometa a cbo:Comet ;
            cbo:firstObservation ?primobs ;
            cbo:hasFullName ?fullname ;
            cbo:hasId ?id ;
            cbo:hasName ?name ;
            cbo:hasOberservations ?obs ;
            cbo:hasOrbit ?orbit ;
            cbo:hasPrimaryDesignation ?pdes ;
            cbo:lastObservation ?lastobs ;
        OPTIONAL { ?cometa owl:sameAs ?dbpedia }

    }
    """,initBindings={'cometa': URIRef(uri)})
    for row in comet:
        res.append({
            'name' : row.name,
            'fullname' : row.fullname,
            'orbit' : row.orbit,
            'id' : row.id,
            'primobs' : row.primobs,
            'lastobs' : row.lastobs,
            'pdes' : row.pdes,
            'dbpedia' : row.dbpedia,
            'obs' : row.obs
        })
    return res

def find_body_name(uri):
    res = []
    body = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?fullname
    WHERE {
        ?body a ?celestialbody ;
            cbo:hasFullName ?fullname ;
    }
    """,initBindings={'body': URIRef(uri)}
    )
    for row in body:
        fullname = row.fullname.toPython()
        res.append(fullname)
    return res


def asteroid_by_uri(uri):
    res = []
    asteroid = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?primobs ?fullname ?id ?name ?obs ?orbit ?pdes ?lastobs ?dbpedia 
    WHERE {
        ?asteroide a cbo:Asteroid ;
            cbo:firstObservation ?primobs ;
            cbo:hasFullName ?fullname ;
            cbo:hasId ?id ;
            cbo:hasName ?name ;
            cbo:hasOberservations ?obs ;
            cbo:hasOrbit ?orbit ;
            cbo:hasPrimaryDesignation ?pdes ;
            cbo:lastObservation ?lastobs ;
        OPTIONAL { ?asteroide owl:sameAs ?dbpedia }
        OPTIONAL { ?asteroide cbo:hasName ?name }

    }
    """,initBindings={'asteroide': URIRef(uri)})
    for row in asteroid:
        res.append({
            'name' : row.name,
            'fullname' : row.fullname,
            'orbit' : row.orbit,
            'id' : row.id,
            'primobs' : row.primobs,
            'lastobs' : row.lastobs,
            'pdes' : row.pdes,
            'dbpedia' : row.dbpedia,
            'obs' : row.obs
        })
    return res

def orbit_by_class(classe):
    res = []
    orbita = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?orbita
    WHERE {
        ?orbita a cbo:Orbit ;
            cbo:category ?cat ;
        FILTER (?cat = ?classe)
    }
    """,initBindings={'classe': Literal(classe)})

    for row in orbita:
        uri = row.orbita.toPython()
        orbit_num = uri.split("/")[-1]
        res.append(orbit_num)
    return res

def orbit_by_oid(id):
    res = []
    orbita = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?orbita
    WHERE {
        ?orbita a cbo:Orbit ;
            cbo:hasOrbitId ?id ;
         FILTER (?id = ?oid)
    }
    """,initBindings={'oid': Literal(id)})

    for row in orbita:
        uri = row.orbita.toPython()
        orbit_num = uri.split("/")[-1]
        res.append(orbit_num)
    return res

def orbita_all(nome_r):
    res = []
    orbita = g.query(
    """
    PREFIX cbo: <http://www.celestial.bodies.org/ontology/>
    PREFIX cbr: <http://www.celestial.bodies.org/resource/>

    SELECT ?cat ?id ?e ?i ?node ?ms ?moid ?pa ?prod ?ta ?of
    WHERE {
        ?orbita a cbo:Orbit ;
            cbo:category ?cat ;
            cbo:hasOrbitId ?id ;
            cbo:hasEccentricity ?e ;
            cbo:hasInclination ?i ;
            cbo:hasLongitudeOfTheAscendingNode ?node ;
            cbo:hasMajorSemiaxis ?ms;
            cbo:hasMinimumOrbitIntersectionDistance ?moid;
            cbo:hasPerihelionArgument ?pa ;
            cbo:hasTrueAnomaly ?ta ;
            cbo:orbitOf ?of ;
        OPTIONAL{ ?orbita cbo:hasProducer ?prod }
    }
    """,initBindings={'orbita': URIRef(nome_r)})

    for row in orbita:
        res.append({
            'cat' : row.cat,
            'id' : row.id,
            'e' : row.e,
            'i' : row.i,
            'node' : row.node,
            'ms' : row.ms,
            'moid' : row.moid,
            'pa' : row.pa,
            'prod' : row.prod,
            'ta' : row.ta,
            'of' : row.of
        })
    return res
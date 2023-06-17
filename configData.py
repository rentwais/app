# Este archivo contiene variables necesarias en app.py
# es necesario importar este archivo para poder disponer de estos datos

numero_parametros = 167

# localidad
barrios = {
    'palacio':'centro',
    'lavapiés-embajadores':'centro',
    'huertas-cortes':'centro',
    'justicia':'centro',
    'malasaña-universidad':'centro',
    'sol':'centro',
    'chuecajusticia':'centro',

    'imperial':'arganzuela',
    'acacias':'arganzuela',
    'chopera':'arganzuela',
    'legazpi':'arganzuela',
    'delicias':'arganzuela',
    'palosdelafrontera':'arganzuela',
    'palosdemoguer':'arganzuela',
    'atocha':'arganzuela',

    'pacífico':'retiro',
    'adelfas':'retiro',
    'estrella':'retiro',
    'ibiza':'retiro',
    'jerónimos':'retiro',
    'niñojesús':'retiro',     

    'recoletos':'salamanca',
    'goya':'salamanca',
    'fuentedelberro':'salamanca',
    'guindalera':'salamanca',
    'lista':'salamanca',
    'castellana':'salamanca',
    'barriodesalamanca':'salamanca',

    'elviso':'chamartin',
    'prosperidad':'chamartin',
    'ciudadjardin':'chamartin',
    'hispanoamerica':'chamartin',
    'nuevaespana':'chamartin',
    'castilla':'chamartin',
    'chamartín':'chamartin',  

    'bellasvistas':'tetuan',
    'cuatrocaminos':'tetuan',
    'ventilla-almenara':'tetuan',
    'valdeacederas':'tetuan',
    'berruguete':'tetuan',
    'cuzco-castillejos':'tetuan',
    'tetuán':'tetuan',  

    'gaztambide':'chamberi',
    'arapiles':'chamberi',
    'trafalgar':'chamberi',
    'almagro':'chamberi',
    'nuevosministerios-ríosrosas':'chamberi',
    'vallehermoso':'chamberi',
    'chamberí':'chamberi',  

    'elpardo':'fuencarral',
    'fuentelarreina':'fuencarral',
    'peñagrande':'fuencarral',    
    'pilar':'fuencarral',
    'lapaz':'fuencarral',
    'mirasierra':'fuencarral',
    'elgoloso':'fuencarral',
    'arroyodelfresno':'fuencarral',
    'lastablas':'fuencarral',     
    'montecarmelo':'fuencarral',  
    'tresolivos-valverde':'fuencarral',  

    'casadecampo':'moncloa',
    'arguelles':'moncloa',
    'argüelles':'moncloa',
    'ciudaduniversitaria':'moncloa',
    'valdezarza':'moncloa',
    'valdemarín':'moncloa', 
    'elplantío':'moncloa',  
    'aravaca':'moncloa',

    'loscarmenes':'latina',
    'puertadelangel':'latina',
    'lucero':'latina',
    'aluche':'latina',
    'campamento':'latina',
    'cuatrovientos':'latina',
    'aguilas':'latina',

    'comillas':'carabanchel',
    'opañel':'carabanchel', 
    'sanisidro':'carabanchel',
    'vistaalegre':'carabanchel',
    'puertabonita':'carabanchel',
    'buenavista':'carabanchel',
    'abrantes':'carabanchel',
    'paudecarabanchel':'carabanchel',   

    '12deoctubre-orcasur':'usera',
    'orcasitas':'usera',
    'orcasur':'usera',
    'sanfermín':'usera',    
    'almendrales':'usera',
    'moscardó':'usera',             
    'zofío':'usera',
    'pradolongo':'usera',

    'entrevías':'puente-de-vallecas',   
    'sandiego':'puente-de-vallecas',
    'palomerasbajas':'puente-de-vallecas',
    'palomerassureste':'puente-de-vallecas',
    'portazgo':'puente-de-vallecas',
    'numancia':'puente-de-vallecas',
    'puente-de-vallecas':'puente-de-vallecas',
    'puentedevallecas':'puente-de-vallecas',

    'pavones':'moratalaz',
    'horcajo':'moratalaz',
    'marroquina':'moratalaz',
    'medialegua':'moratalaz',
    'fontarrón':'moratalaz',        
    'vinateros':'moratalaz',
    'moratalaz':'moratalaz',

    'ventas':'ciudadlineal',
    'pueblonuevo':'ciudadlineal',
    'quintana':'ciudadlineal',
    'concepción':'ciudadlineal',    
    'sanpascual':'ciudadlineal',
    'sanjuanbautista':'ciudadlineal',
    'colina':'ciudadlineal',
    'atalaya':'ciudadlineal',
    'costillares':'ciudadlineal',
    'ciudadlineal':'ciudadlineal',  

    'palomas':'hortaleza',
    'canillas':'hortaleza',
    'pinardelrey':'hortaleza',
    'apostolsantiago':'hortaleza',
    'valdebebas-valdefuentes':'hortaleza',
    'condeorgaz-piovera':'hortaleza',     
    'sanchinarro':'hortaleza',
    'virgendelcortijo-manoteras':'hortaleza',     

    'sancristóbal':'villaverdealto',
    'butarque':'villaverdealto',
    'losrosales':'villaverdealto',
    'losángeles':'villaverdealto',  
    'villaverdealto':'villaverdealto',  

    'cascohistóricodevallecas':'villadevallecas',
    'villadevallecas':'villadevallecas', 
    'santaeugenia':'villadevallecas',
    'ensanchedevallecas-lagavia':'villadevallecas',

    'cascohistóricodevicálvaro':'vicalvaro',
    'vicálvaro':'vicalvaro',
    'valdebernardo':'vicalvaro',
    'valdebernardo-valderrivas':'vicalvaro',
    'elcañaveral':'vicalvaro',  
    'ambroz':'vicalvaro',       

    'simancas':'sanblas',
    'hellín':'sanblas',         
    'amposta':'sanblas',
    'arcos':'sanblas',
    'rosas':'sanblas',
    'rejas':'sanblas',
    'canillejas':'sanblas',
    'salvador':'sanblas',       
    'sanblas':'sanblas',        

    'alamedadeosuna':'barajas',
    'aeropuerto':'barajas',
    'cascohistoricodebarajas':'barajas',
    'timón':'barajas',
    'corralejos':'barajas',
    'campodelasnaciones-corralejos':'barajas',  #
    'cascohistóricodebarajas':'barajas'     
}

features = ['metros', 'habitaciones', 'baños', 'planta', 'ascensor', 'exterior', 'equipada', 'amueblada', 'garaje', 'terraza', 'aireacondicionado', 'distrito_arganzuela', 'distrito_barajas', 'distrito_carabanchel', 'distrito_centro', 'distrito_chamartin', 'distrito_chamberi', 'distrito_ciudadlineal', 'distrito_fuencarral', 'distrito_hortaleza', 'distrito_moncloa', 'distrito_moratalaz', 'distrito_puentedevallecas', 'distrito_retiro', 'distrito_salamanca', 'distrito_sanblas', 'distrito_tetuan', 'distrito_usera', 'distrito_vicalvaro', 'distrito_villadevallecas', 'distrito_villaverde', 'tipovivienda_Dúplex', 'tipovivienda_Estudio', 'tipovivienda_Piso', 'tipovivienda_Ático', 'tipovivienda_nan', 'calefaccion_0', 'calefaccion_central', 'calefaccion_individual', 'localidad_12deoctubreorcasur', 'localidad_abrantes', 'localidad_acacias', 'localidad_adelfas', 'localidad_alamedadeosuna', 'localidad_almagro', 'localidad_almendrales', 'localidad_ambroz', 'localidad_amposta', 'localidad_arapiles', 'localidad_aravaca', 'localidad_arcos', 'localidad_argüelles', 'localidad_arroyodelfresno', 'localidad_atalaya', 'localidad_barriodesalamanca', 'localidad_bellasvistas', 'localidad_berruguete', 'localidad_buenavista', 'localidad_butarque', 'localidad_campodelasnacionescorralejos', 'localidad_canillejas', 'localidad_casadecampo', 'localidad_cascohistóricodebarajas', 'localidad_cascohistóricodevallecas', 'localidad_cascohistóricodevicálvaro', 'localidad_castellana', 'localidad_chamartín', 'localidad_chamberí', 'localidad_chopera', 'localidad_chuecajusticia', 'localidad_ciudadlineal', 'localidad_ciudaduniversitaria', 'localidad_colina', 'localidad_comillas', 'localidad_concepción', 'localidad_condeorgazpiovera', 'localidad_costillares', 'localidad_cuatrocaminos', 'localidad_cuzcocastillejos', 'localidad_delicias', 'localidad_elcañaveral', 'localidad_elpardo', 'localidad_elplantío', 'localidad_ensanchedevallecaslagavia', 'localidad_entrevías', 'localidad_estrella', 'localidad_fontarrón', 'localidad_fuentedelberro', 'localidad_fuentelarreina', 'localidad_gaztambide', 'localidad_goya', 'localidad_guindalera', 'localidad_hellín', 'localidad_horcajo', 'localidad_huertascortes', 'localidad_ibiza', 'localidad_imperial', 'localidad_jerónimos', 'localidad_lapaz', 'localidad_lastablas', 'localidad_lavapiésembajadores', 'localidad_legazpi', 'localidad_lista', 'localidad_losrosales', 'localidad_losángeles', 'localidad_malasañauniversidad', 'localidad_marroquina', 'localidad_medialegua', 'localidad_mirasierra', 'localidad_montecarmelo', 'localidad_moscardó', 'localidad_niñojesús', 'localidad_nuevosministeriosríosrosas', 'localidad_numancia', 'localidad_opañel', 'localidad_orcasitas', 'localidad_pacífico', 'localidad_palacio', 'localidad_palomas', 'localidad_palomerasbajas', 'localidad_palomerassureste', 'localidad_palosdemoguer', 'localidad_paudecarabanchel', 'localidad_pavones', 'localidad_peñagrande', 'localidad_pilar', 'localidad_pinardelrey', 'localidad_portazgo', 'localidad_pradolongo', 'localidad_prosperidad', 'localidad_pueblonuevo', 'localidad_puentedevallecas', 'localidad_puertabonita', 'localidad_quintana', 'localidad_recoletos', 'localidad_rejas', 'localidad_rosas', 'localidad_salvador', 'localidad_sanblas', 'localidad_sanchinarro', 'localidad_sancristóbal', 'localidad_sandiego', 'localidad_sanfermín', 'localidad_sanisidro', 'localidad_sanjuanbautista', 'localidad_sanpascual', 'localidad_simancas', 'localidad_sol', 'localidad_tetuán', 'localidad_timón', 'localidad_trafalgar', 'localidad_tresolivosvalverde', 'localidad_valdeacederas', 'localidad_valdebebasvaldefuentes', 'localidad_valdebernardovalderrivas', 'localidad_valdemarín', 'localidad_valdezarza', 'localidad_vallehermoso', 'localidad_ventas', 'localidad_ventillaalmenara', 'localidad_vicálvaro', 'localidad_villadevallecas', 'localidad_villaverdealto', 'localidad_vinateros', 'localidad_virgendelcortijomanoteras', 'localidad_vistaalegre', 'localidad_zofío']
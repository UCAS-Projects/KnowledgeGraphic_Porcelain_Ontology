import rdflib

def test_ontology():
    # 创建一个图 (Graph) 实例
    g = rdflib.Graph()
    
    # 解析本地的OWL文件 (RDF/XML格式)
    print("正在加载瓷器本体库 (porcelain_ontology.owl)...")
    g.parse("porcelain_ontology.owl", format="xml")
    
    print(f"加载成功！图谱中共有 {len(g)} 个三元组 (Triples)。\n")
    
    # 编写一个SPARQL查询：查找所有“瓷器”实例的名称及其所属窑口和朝代
    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX por: <http://www.example.org/porcelain#>
    
    SELECT ?name ?dynastyLabel ?kilnLabel
    WHERE {
        ?porcelain rdf:type por:Porcelain .
        ?porcelain por:hasName ?name .
        
        ?porcelain por:hasDynasty ?dynasty .
        ?dynasty rdfs:label ?dynastyLabel .
        
        ?porcelain por:hasKiln ?kiln .
        ?kiln rdfs:label ?kilnLabel .
    }
    """
    
    print("执行SPARQL查询：查找所有瓷器名称、朝代及其窑口...")
    results = g.query(query)
    
    print("-" * 40)
    for row in results:
        print(f"瓷器: {row.name}")
        print(f"朝代: {row.dynastyLabel}")
        print(f"窑口: {row.kilnLabel}")
        print("-" * 40)

if __name__ == "__main__":
    try:
        test_ontology()
    except Exception as e:
        print(f"运行失败: {e}\n提示：请确保已安装 rdflib。可以使用 pip install rdflib 安装。")

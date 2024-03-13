import networkx as nx

class CogniGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_cognitive_entity(self, entity_id, attributes=None):
        """
        Add a cognitive entity to the graph.

        Parameters:
        - entity_id: Unique identifier for the cognitive entity.
        - attributes: Dictionary containing attributes of the cognitive entity.
        """
        if attributes is None:
            attributes = {}
        self.graph.add_node(entity_id, **attributes)

    def add_relationship(self, entity1, entity2, relationship_type, weight=1.0):
        """
        Add a relationship between two cognitive entities.

        Parameters:
        - entity1, entity2: Unique identifiers of the cognitive entities.
        - relationship_type: Type of relationship between the entities.
        - weight: Strength of the relationship.
        """
        self.graph.add_edge(entity1, entity2, type=relationship_type, weight=weight)

    def simulate_neuroplasticity(self, entity_id, learning_rate=0.1):
        """
        Simulate neuroplasticity for a cognitive entity.

        Parameters:
        - entity_id: Unique identifier of the cognitive entity.
        - learning_rate: Rate at which the entity adapts to new information.
        """
        for neighbor in self.graph.neighbors(entity_id):
            self.graph[entity_id][neighbor]['weight'] += learning_rate

    def get_entity_attributes(self, entity_id):
        """
        Retrieve attributes of a cognitive entity.

        Parameters:
        - entity_id: Unique identifier of the cognitive entity.

        Returns:
        - Dictionary containing attributes of the cognitive entity.
        """
        return self.graph.nodes[entity_id]

    def get_relationships(self, entity_id):
        """
        Retrieve relationships of a cognitive entity.

        Parameters:
        - entity_id: Unique identifier of the cognitive entity.

        Returns:
        - List of tuples representing relationships (neighbor, type, weight).
        """
        relationships = []
        for neighbor in self.graph.neighbors(entity_id):
            data = self.graph[entity_id][neighbor]
            relationships.append((neighbor, data['type'], data['weight']))
        return relationships

# Example Usage
cogni_graph = CogniGraph()

# Add cognitive entities
cogni_graph.add_cognitive_entity("entity1", {"type": "Neuron"})
cogni_graph.add_cognitive_entity("entity2", {"type": "Concept"})

# Add relationships
cogni_graph.add_relationship("entity1", "entity2", "ConnectsTo", weight=0.8)

# Simulate neuroplasticity
cogni_graph.simulate_neuroplasticity("entity1")

# Get entity attributes and relationships
print(cogni_graph.get_entity_attributes("entity1"))
print(cogni_graph.get_relationships("entity1"))

import unittest

class TestCogniGraph(unittest.TestCase):
    def setUp(self):
        self.cogni_graph = CogniGraph()

    def test_add_cognitive_entity(self):
        self.cogni_graph.add_cognitive_entity("entity1", {"type": "Neuron"})
        attributes = self.cogni_graph.get_entity_attributes("entity1")
        self.assertEqual(attributes, {"type": "Neuron"})

    def test_add_relationship(self):
        self.cogni_graph.add_cognitive_entity("entity1", {"type": "Neuron"})
        self.cogni_graph.add_cognitive_entity("entity2", {"type": "Concept"})
        self.cogni_graph.add_relationship("entity1", "entity2", "ConnectsTo", weight=0.8)

        relationships = self.cogni_graph.get_relationships("entity1")
        self.assertEqual(relationships, [("entity2", "ConnectsTo", 0.8)])

    def test_simulate_neuroplasticity(self):
        self.cogni_graph.add_cognitive_entity("entity1", {"type": "Neuron"})
        self.cogni_graph.add_cognitive_entity("entity2", {"type": "Concept"})
        self.cogni_graph.add_relationship("entity1", "entity2", "ConnectsTo", weight=0.8)

        self.cogni_graph.simulate_neuroplasticity("entity1")
        relationships_after_plasticity = self.cogni_graph.get_relationships("entity1")
        # Check that weights have increased
        self.assertGreater(relationships_after_plasticity[0][2], 0.8)

if __name__ == '__main__':
    unittest.main()


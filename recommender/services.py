from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Domain

def recommend_domains(query):
    # Handle None or empty query
    if not query or query.strip() == "":
        # Return all domains if no query provided
        domains = Domain.objects.all()
        return [(d, 0) for d in domains]

    domains = Domain.objects.all()

    corpus = []
    domain_list = []

    for d in domains:
        text = d.name + " " + d.skills + " " + d.description
        corpus.append(text)
        domain_list.append(d)

    corpus.append(query.strip())

    try:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(corpus)

        similarity = cosine_similarity(vectors[-1], vectors[:-1]).flatten()

        ranked = sorted(
            zip(domain_list, similarity),
            key=lambda x: x[1],
            reverse=True
        )

        # Filter results with minimum similarity threshold (0.1 = 10%)
        min_threshold = 0.1
        filtered_results = [(d, score * 100) for d, score in ranked if score >= min_threshold]

        return filtered_results
    except Exception as e:
        # If vectorization fails, return empty list
        print(f"Error in recommend_domains: {e}")
        return []
from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
    {"id": 1, "name": "The Shawshank Redemption", "genre": "Drama"},
    {"id": 2, "name": "The Godfather", "genre": "Drama"},
    {"id": 3, "name": "The Dark Knight", "genre": "Action"},
    {"id": 4, "name": "12 Angry Men", "genre": "Drama"},
    {"id": 5, "name": "Schindler's List", "genre": "Drama"},
    {"id": 6, "name": "The Lord of the Rings: The Return of the King", "genre": "Fantasy"},
    {"id": 7, "name": "Pulp Fiction", "genre": "Crime"},
    {"id": 8, "name": "Forrest Gump", "genre": "Drama"},
    {"id": 9, "name": "The Matrix", "genre": "Action"},
    {"id": 10, "name": "The Silence of the Lambs", "genre": "Thriller"}
]


@app.route('/movies', methods=['GET', 'POST'])
def movies_handler():
    if request.method == 'POST':
        new_movie = request.json
        new_movie['id'] = max(movie['id'] for movie in movies) + 1
        movies.append(new_movie)
        return jsonify(new_movie), 201
    else:
        return jsonify(movies)


@app.route('/movies/<int:movie_id>')
def get_movie(movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id), None)
    if movie:
        return jsonify(movie)
    else:
        return jsonify({'error': 'Movie not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)

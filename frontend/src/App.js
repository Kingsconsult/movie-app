import React, { Component } from "react";
import "./App.css";
import MovieList from "./components/movieList";

class App extends Component {
  // movies = ["titanic", "avatar"];

  state = {
    movies: []
  };

  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/movies/", {
      method: "GET",
      headers: {
        Authorization: "Token 7639950cadfe4f31165e7600ed69bd4644a66465"
      }
    })
      .then(resp => resp.json())
      .then(res => this.setState({ movies: res }))
      .catch(error => console.log(error));
  }

  // componentDidMount() {
  //   fetch("https://swapi.co/api/people/", {
  //     method: "GET",

  //   })
  //     .then(resp => resp.json())
  //     .then(res => this.setState({ movies: res }))
  //     .catch(error => console.log(error));
  // }

  render() {
    return (
      <div className="App">
        <h1>Movie Rater</h1>
        <MovieList movies={this.state.movies} />
      </div>
    );
  }
}

export default App;

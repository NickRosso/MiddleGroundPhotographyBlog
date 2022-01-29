
import React, { Component } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import PostList from "./PostList"; 

export default class Home extends Component {
    constructor(props) {
        super(props);
        this.state = {
          viewPublished: false,
        };
      };

    displayPublished = status => {
        if (status) {
          return this.setState({ viewPublished: true});
        }
        return this.setState({ viewPublished: false});
      };
    
      renderTabList = () => {
        return (
          <div className="my-5 tab-list">
            <button 
              onClick={() => this.displayPublished(true)}
              className={this.state.viewPublished ? 1 : ""}
            >
              Published
            </button>
            <button 
              onClick={() => this.displayPublished(false)}
              className={this.state.viewPublished ? "" : 0}
            >
              Unpublished
            </button>
          </div>  
        );
      };
    
    render() {
        return (
        <content>
            <h1 className="text-white text-uppercase text-center my-4">Middle Ground Posts</h1>
            <div className="row">
            <div className="col-md-6 col-sm-10 mx-auto p-0">
                <div className="card p-3">
                {this.renderTabList()}
                <ul className="list-group list-group-flush">
                    <PostList />
                </ul>
                </div>
            </div>
            </div>
        </content>
        );
    }
}
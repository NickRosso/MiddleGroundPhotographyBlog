import React, { Component } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import ImageCarousel from "./ImageCarousel"; 
import {
    Card,
    CardBody,
    CardImg,
    CardTitle,
    CardSubtitle,
    CardText,
    Button,
} from "reactstrap";


export default class Post extends Component {
    constructor(props) {
        super(props);
        this.state = {
            post: this.props.post,
            recentPosts: []
        };
    }

    async componentDidMount() {
        try {
          const res = await fetch('http://127.0.0.1:8000/Posts/');
          const recentPosts = await res.json();
          this.setState({
            recentPosts
          });
        } catch (e){
          console.log(e);
        }
      }

    renderPosts = () => {
        const { viewPublished } = this.state;
        const newPosts = this.state.recentPosts.filter(
            item => item.status === 1
        );
        return newPosts.map(post => (
        <Card>
            <CardBody>
                <CardTitle tag="h5">
                    {post.title}
                </CardTitle>
                <CardSubtitle
                    className="mb-2 text-muted"
                    tag="h6"
                >
                    By: {post.author.first_name}, {post.author.last_name}
                </CardSubtitle>
                <ImageCarousel album={post.album} />
                <CardText>
                    {post.content}
                    Created on: {post.created_at}
                </CardText>
                <Button>
                    View
                </Button>
            </CardBody>
        </Card>
        ));
    };
    render() {
        return (
            this.renderPosts()
        );
    }
}
import React from "react";
import { Button, Grid, Row, Col, Form, FormGroup, ControlLabel, FormControl } from "react-bootstrap";
import DetailedView from "./DetailedView"
import $ from 'jquery'
// import wool from '../images/wool.svg';

// import Icon from "./wool.svg";
// import svgSource from ‘./wool.svg’

// const SVG = () => 
//   <svg
//     width="100%"
//     height="100%"
//     viewBox="0 0 32 32"
//     xmlns="http://www.w3.org/2000/svg"
//     xmlnsXlink="http://www.w3.org/1999/xlink"
//   >
//       <path d="./wool.svg" fill="#000" />
//   </svg>;



export default class SearchResults extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          data: [
            {
                name: "mini_pattern.name",
                pattern_id: "mini_pattern.pattern_id",
                img_fullsize_url : "mini_pattern.img_fullsize_url",
                img_small_url : "mini_pattern.img_small_url"
            }
           ],
           pattern: {
                pattern_id: this.props.pattern_id
           },
           isQueueSelection : this.props.isQueueSelection,
           isSearchResultsSelection : false,
           page_number: 1,
           query : this.props.query,
           user: {
                email : this.props.email,
                is_logged_in : this.props.is_logged_in
            }
        };

        this.getPatternID = this.getPatternID.bind(this);
        this.getNextPage = this.getNextPage.bind(this);
        this.getPreviousPage = this.getPreviousPage.bind(this);
    }


    setMiniPatterns(mini_patterns_list){
        /*
            Sets new state of component using mini patterns list.
        */
        this.setState({
            data : mini_patterns_list
        });

    }


    getPythonMiniPatternsByQuery(query, next_page){
        /*
            Returns mini pattern search result by given query string and page number.
        */

        const route_query = '/patterns/knitting/query/'
        const route_page = '/page/'

        this.setState({
            page_number : next_page,
            query : query
        })

        $.get(route_query + query + route_page + next_page, (data) => {
            console.log(data);
            this.setMiniPatterns(data)
        });
    }


    setPage(increment, decrement){
        /*
            Sets page number to use for api call. 
            If current page is first page and user tries to get previous page,
            no call is executed.
        */

        const query = this.state.query

        if (increment){
            this.getPythonMiniPatternsByQuery(query, this.state.page_number + 1)
        }else{
            if(decrement){
                if (this.state.page_number > 1){
                    this.getPythonMiniPatternsByQuery(query, this.state.page_number - 1)
                }else{
                    console.log('No previous page! Already on page '+ this.state.page_number)
                }
            }else{
                this.getPythonMiniPatternsByQuery(query, this.state.page_number)
            }
        };

    }


    getPatternID(pattern_id){
        /*
            Gets pattern_id from selected mini pattern.
        */
        console.log('Click! getPatternID:')
        console.log(pattern_id)

        this.setState({
            pattern: {
                pattern_id : pattern_id
            },
            isQueueSelection : false,
            isSearchResultsSelection : true
        });

    };


    getNextPage(){
        /*
            Gets next page of results.
        */

        this.setPage(true, false); 
    }


    getPreviousPage(){
        /*
            Gets previous page of results.
        */

        this.setPage(false, true); 
    }


    componentDidMount() {
        this.getPythonMiniPatternsByQuery(this.state.query, 1); 
    }


    componentWillReceiveProps(nextProps){
        let isDifferentQuery = (nextProps.query != this.state.query ? true : false)
        let hasChangedLogIn = (nextProps.is_logged_in != this.state.user.is_logged_in ? true : false)
        let isDifferentPatternID = (nextProps.pattern_id != this.state.pattern.pattern_id ? true : false)

        // console.log('++++++++++ nextProps.isQueueSelection')
        // console.log(nextProps.isQueueSelection)
        if(isDifferentQuery){

            this.getPythonMiniPatternsByQuery(nextProps.query, 1);

            this.setState({
                user: {
                    email : nextProps.email,
                    is_logged_in : nextProps.is_logged_in
                }
            });
        }else if(hasChangedLogIn){
            this.setState({
                user: {
                    email : nextProps.email,
                    is_logged_in : nextProps.is_logged_in
                }
            });

        }else if(isDifferentPatternID){
            if(nextProps.isQueueSelection){
                // console.log('@@@@@@@@@@@@@ nextProps.isQueueSelection')
                // console.log(nextProps.isQueueSelection)
                this.setState({
                    pattern: {
                        pattern_id : nextProps.pattern_id
                    },
                    isQueueSelection : true,
                    isSearchResultsSelection : false
                })
            }
        }

    }


    render(){
        return (
            <div>
                <Row>
                <Col md={7}>
                    <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam varius efficitur nulla ut condimentum. Suspendisse rhoncus massa vitae dolor dapibus, sit amet feugiat mauris rhoncus. Nam sapien felis, sagittis at sapien quis, vulputate vehicula ligula. Sed ac egestas justo, at fringilla est. Nam eleifend, nisl vitae maximus sagittis, felis massa dapibus elit, in pharetra justo ex non eros.
                    </p>
                    <p>
                        <Button bsStyle="danger" onClick={this.getPreviousPage} className="mr-sm-2">
                          Previous Page
                        </Button>
                        <Button  bsStyle="danger" onClick={this.getNextPage} className="mr-sm-2">
                          Next Page
                        </Button>
                    </p>
                    <div id="searchResults">
                    {this.state.data.map(d => 
                        <div key={d.pattern_id} onClick={()=>this.getPatternID(d.pattern_id)} className="float-left">
                            <img className="mini_pattern" src={d.img_small_url}/>
                        </div>
                    )}
                    </div>
                </Col>
                <Col md={5}>
                    <DetailedView pattern_id={this.state.pattern.pattern_id} is_logged_in={this.state.user.is_logged_in} email={this.state.user.email} isQueueSelection={this.state.isQueueSelection} isSearchResultsSelection={this.state.isSearchResultsSelection}/> 
                </Col> 
                </Row>
            </div>
            );
    }

}


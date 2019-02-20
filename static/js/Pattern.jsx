import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";


// var $ = require('jquery');
import $ from 'jquery'

export default class Pattern extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            name: 'pattern.name' ,
            author : 'pattern.author',
            created_at: 'pattern.created_at',
            pattern_type: 'pattern.pattern_type',
            sizes: 'pattern.sizes',
            yardage: 'pattern.yardage',
            yarn_weight : 'pattern.yarn_weight',
            gauge : 'pattern.gauge',
            is_clothing : 'pattern.is_clothing',
            is_free : 'pattern.is_free',
            is_downloadable : 'pattern.is_downloadable',
            download_url : 'pattern.url',
            description : 'pattern.description',
            img_fullsize_url : 'pattern.img_fullsize_url',
            img_small_url: 'pattern.img_small_url',
            suggested_yarn : 'pattern.suggested_yarn',
            needles_required : 'pattern.needles',
            pattern_id : this.props.id
        };

        this.getPythonPattern = this.getPythonPattern.bind(this);

    }

    getYarnText(yarn){
        /*
            Returns a yarn item by combining name and weight to one string.
        */
        const yarn_html = yarn.name + ' (' + yarn.weight + ')'

        return yarn_html
    }

    getSuggestedYarn(yarn_list){
        /*
            Returns list with yarn name and weight.
        */
        const yarn_unpacked = []

        for(let i = 0; i< yarn_list.length; i++){
            const yarn = this.getYarnText(yarn_list[i])
            yarn_unpacked.push(yarn)

        };

        return yarn_unpacked
    }

    getNeedlesRequired(needles_list){
        /*
            Returns list with needle names.
        */
        const needles_unpacked = []

        for(let i = 0; i< needles_list.length; i++){
            const needles = needles_list[i]['name']
            needles_unpacked.push(needles)

        };

        return needles_unpacked

    }

    getBoolString(bool_to_convert){
        /*
            Converts boolean values to string.
        */

        if (bool_to_convert){
            return 'Yes'
        }else{
            return 'No'
        }

    }


    setListItems(items_list, obj_to_map){

        return items_list.map((obj_to_map) =>
            <li key={obj_to_map.toString()}>
            {obj_to_map}</li>
            );
    }


    setPattern(pattern_list){
        /* 
            Sets new state of component with pattern values.
        */

        const pattern = pattern_list[0]

        const suggested_yarn = this.getSuggestedYarn(pattern.suggested_yarn)
        
        const needles_required = this.getNeedlesRequired(pattern.needles)

        let is_free_string = this.getBoolString(pattern.is_free)

        let is_downloadable_string = this.getBoolString(pattern.is_downloadable)
 
        const yarn_list = this.setListItems(suggested_yarn, 'yarn')
        const needles_required_list = this.setListItems(needles_required, 'needles')
             

        this.setState({
            name: pattern.name ,
            author : pattern.author,
            created_at: pattern.created_at,
            pattern_type: pattern.pattern_type,
            sizes: pattern.sizes,
            yardage: pattern.yardage,
            yarn_weight : pattern.yarn_weight,
            gauge : pattern.gauge,
            is_clothing : pattern.is_clothing,
            is_free : is_free_string,
            is_downloadable : is_downloadable_string,
            download_url : pattern.url,
            description : pattern.description,
            img_fullsize_url : pattern.img_fullsize_url,
            img_small_url: pattern.img_small_url,
            suggested_yarn : yarn_list,
            needles_required : needles_required_list
        });

    }


    getPythonPattern(pattern_id){
        /* 
            Gets pattern info from python server and forwards it to set the new state of component.
        */

        // const pattern_id = this.state.pattern_id;


        if (pattern_id != this.state.pattern_id){
            this.setState({
                pattern_id : pattern_id
            })
        }

        const route = '/patterns/knitting/ids/';

        $.get(route + pattern_id, (data) => {
            console.log(data);
            this.setPattern(data)
        });
    }

    componentDidMount() {
        this.getPythonPattern(this.state.pattern_id); 
    }

    componentWillReceiveProps(nextProps){
        this.getPythonPattern(nextProps.id)

    }


    render () {
        return (
                <Col>
                    <h1>{this.state.name}</h1>
                    By {this.state.author}
                    <br></br>
                    Created at {this.state.created_at}
                    <hr/>
                    <img src={this.state.img_fullsize_url}/>
                    <p>
                    Pattern Type: {this.state.pattern_type}
                    <br></br>
                    Available sizes: {this.state.sizes}
                    <br></br>
                    Yardage: {this.state.yardage}
                    <br></br>
                    Yarn weight: {this.state.yarn_weight}
                    <br></br>
                    Gauge: {this.state.gauge}
                    <br></br>
                    Is it free?: {this.state.is_free}
                    <br></br>
                    Can I download it?: {this.state.is_downloadable}
                    <br></br>
                    Download url: {this.state.download_url}
                    </p>
                    Suggested Yarn: 
                    <ul>
                    {this.state.suggested_yarn}
                    </ul>
                    Needles required:
                    <ul>
                    {this.state.needles_required}
                    </ul>
                    <p>
                    Description: {this.state.description}
                    </p>
                </Col>
        );
    }

}
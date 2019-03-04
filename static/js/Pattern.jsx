import React from "react";
import { Button, Grid, Row, Col } from "react-bootstrap";


// var $ = require('jquery');
import $ from 'jquery'

export default class Pattern extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            data : {
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
            },
           pattern_id : this.props.pattern_id,
           count_queues : '0',
           user: {
                email : this.props.email,
                is_logged_in : this.props.is_logged_in
            },
            is_in_queue : false
        };

        this.getPythonPattern = this.getPythonPattern.bind(this);
        this.addToQueue = this.addToQueue.bind(this);
        this.removeFromQueue = this.removeFromQueue.bind(this);

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
            Converts boolean values to string representation.
        */

        if (bool_to_convert){
            return 'Yes'
        }else{
            return 'No'
        }

    }


    setListItems(items_list, obj_to_map){
        /*
            Returns html representation of items in list.
        */
        return items_list.map((obj_to_map) =>
            <li key={obj_to_map.toString()}>
            {obj_to_map}</li>
            );
    }


    setCountQueues(count_queues){
        /*
            Sets how many times pattern has been added to queue.
        */
        this.setState({
            count_queues : count_queues
        });
    }


    setPattern(pattern_list, count_queues){
        /* 
            Sets pattern values in state.
        */

        const pattern = pattern_list[0]

        const suggested_yarn = this.getSuggestedYarn(pattern.suggested_yarn)
        
        const needles_required = this.getNeedlesRequired(pattern.needles)

        let is_free_string = this.getBoolString(pattern.is_free)

        let is_downloadable_string = this.getBoolString(pattern.is_downloadable)
 
        const yarn_list = this.setListItems(suggested_yarn, 'yarn')
        const needles_required_list = this.setListItems(needles_required, 'needles')
             

        this.setState({
            data : {
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
                needles_required : needles_required_list,
            }
        });



    }

    setPatternIsInQueue(is_in_queue){
        /*
            Sets whether pattern is in user's queue.
        */
        this.setState({
            is_in_queue : is_in_queue
        })

    }

    getPythonPattern(pattern_id){
        /* 
            Gets pattern info from python server and forwards it to set the new state of component.
        */

        // console.log('*******************')
        // console.log('Pattern getPythonPattern:')
        // console.log('this.state:')
        // console.log(this.state.pattern_id)
        // console.log('pattern_id param:')
        // console.log(pattern_id)

        const route = '/patterns/knitting/get/';
        const route_count_queues_pre = '/patterns/knitting/';
        const route_count_queues_post = '/queues/get';

        if (pattern_id){
            $.get(route + pattern_id, (data) => {
            console.log(data);
            $.get(route_count_queues_pre + pattern_id + route_count_queues_post, (data2)=>{
                this.setPattern(data)
                this.setCountQueues(data2['count_queues'])

            });
        });

        }
    }


    isInFavorites(pattern_id_list, pattern_id){
        /*
            Returns true if given pattern_id is in list, false otherwise.
        */
        // console.log('@@@@@@@@@@@@@@@@@@@@@@@')
        for(let i = 0; i<pattern_id_list.length; i++){
            // console.log('pattern_id_list:')
            // console.log(pattern_id_list[i].pattern_id)
            // console.log('pattern_id')
            // console.log(pattern_id)
            if(pattern_id_list[i].pattern_id == pattern_id){
                // console.log('Inside FAV list!')
                return true
            }
        }

        return false
    }

   getFavoritesList(email, pattern_id){
        /*
            Returns list with pattern_id and pattern_name from patterns in favorites list.
        */
        // const email = this.state.user.email
        const route_pre = '/'
        const route_post = '/favorites/get'


        $.get(route_pre + email + route_post, (data) => {    
            // console.log('FAVORITES')
            // console.log(data)
            let isInFavs = this.isInFavorites(data, pattern_id)
            // console.log('######')
            // console.log(isInFavs)
            this.setPatternIsInQueue(isInFavs)
        });

    }

    getPatternIsInQueue(email, pattern_id){
        /*
            Checks if pattern is in user's queue.
        */
        this.getFavoritesList(email, pattern_id)

    }

    addToQueue(){
        /*
            Adds pattern to favorites queue if user is logged in.
        */

        if(this.state.user.is_logged_in == true){
            console.log('Adding to favorites!')

            const email = this.state.user.email
            const pattern_id = this.state.pattern_id

            console.log('pattern_id:')
            console.log(pattern_id)

            const route_pre = '/'
            const route_post = '/favorites/add/'

            const route_count_queues_pre = '/patterns/knitting/';
            const route_count_queues_post = '/queues/get';

            $.get(route_pre + email + route_post + pattern_id, (data) => {
                $.get(route_count_queues_pre + pattern_id + route_count_queues_post, (data2)=>{
                    console.log('Add to queue, return from server:')
                    console.log(data)
                    this.setCountQueues(data2['count_queues'])
                    if(data['success'] == 'true'){
                        this.setPatternIsInQueue(true)
                    }
                });
            });

        }else{
            console.log('You\'re not logged in! Can\'t add to favorites!')
        }
    }

    removeFromQueue(){
        /*
            Removes pattern from user's queue.
        */
        console.log('@@@@@@')
        console.log('Is_In_Queue:')
        console.log(this.state.is_in_queue)
        if(this.state.is_in_queue){
            console.log('Removing from queue!')
            // this.setPatternIsInQueue(false)

            // const email = this.state.user.email
            // const pattern_id = this.state.pattern_id

            // console.log('pattern_id:')
            // console.log(pattern_id)

            // const route_pre = '/'
            // const route_post = '/favorites/add/'

            // const route_count_queues_pre = '/patterns/knitting/';
            // const route_count_queues_post = '/queues/get';

            // $.get(route_pre + email + route_post + pattern_id, (data) => {
            //     $.get(route_count_queues_pre + pattern_id + route_count_queues_post, (data2)=>{
            //         console.log('Add to queue, return from server:')
            //         console.log(data)
            //         this.setCountQueues(data2['count_queues'])
            //         this.setPatternIsInQueue(true)
            //     });
            // });
        }else{
            console.log('Not in user\'s queue! Can\'t remove it.')
        }


    }


    setPatternID(pattern_id){
        /*
            Sets pattern id in state.
        */
        this.setState({
            pattern_id : pattern_id
        })
    }

    setUserAndIfPatternInQueue(user, pattern_id){
        /*
            Sets user information in state.
        */
        this.setState({
            user: {
                email : user.email,
                is_logged_in : user.is_logged_in
            }
        })

        if(user.email && user.is_logged_in){
            this.getPatternIsInQueue(user.email, pattern_id)
        }

    }


    componentDidMount() {
        this.getPythonPattern(this.state.data.pattern_id); 

    }

    componentWillReceiveProps(nextProps){
        this.getPythonPattern(nextProps.pattern_id)
        this.setPatternID(nextProps.pattern_id)
        this.setUserAndIfPatternInQueue(nextProps, nextProps.pattern_id)

    }


    render () {
        return (
                <Col>
                    <h1>{this.state.data.name}</h1>
                    By {this.state.data.author}
                    <br></br>
                    Created at {this.state.data.created_at}
                    <br></br>
                    {this.state.count_queues} ❤ 
                    <br></br>
                    <div>

                    { this.state.user.is_logged_in && this.state.is_in_queue
                        ?
                        <Button key='removeFromQueue' bsStyle="danger" onClick={this.removeFromQueue} className="mr-sm-2" size="sm" >
                        Remove from Favs
                        </Button>
                        : null 
                    }
                    { this.state.user.is_logged_in && !this.state.is_in_queue
                        ?
                        <Button key='addToQueue' bsStyle="danger" onClick={this.addToQueue} className="mr-sm-2" size="sm" >
                        Add to Favs
                        </Button>
                        : null
                    }

                  </div>
                    <hr/>
                    <img src={this.state.data.img_fullsize_url}/>
                    <p>
                    Pattern Type: {this.state.data.pattern_type}
                    <br></br>
                    Available sizes: {this.state.data.sizes}
                    <br></br>
                    Yardage: {this.state.data.yardage}
                    <br></br>
                    Yarn weight: {this.state.data.yarn_weight}
                    <br></br>
                    Gauge: {this.state.data.gauge}
                    <br></br>
                    Is it free?: {this.state.data.is_free}
                    <br></br>
                    Can I download it?: {this.state.data.is_downloadable}
                    <br></br>
                    Download url: {this.state.data.download_url}
                    </p>
                    Suggested Yarn: 
                    <ul>
                    {this.state.data.suggested_yarn}
                    </ul>
                    Needles required:
                    <ul>
                    {this.state.data.needles_required}
                    </ul>
                    <p>
                    Description: {this.state.data.description}
                    </p>
                </Col>
        );
    }

}
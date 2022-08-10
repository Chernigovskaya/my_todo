import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/user.js';
import MenuList from './components/menu.js';
import FooterList from './components/footer.js';
import axios from 'axios';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }
    componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/usersapp/').then(response => {

    this.setState(
            {
                'users': response.data
            }
        )
    }).catch(error => console.log(error))
    }

    render(){
        return (
            <div>
                <MenuList />
                <UserList users={this.state.users} />
                <FooterList />
            </div>
        )
    }
}

export default App;

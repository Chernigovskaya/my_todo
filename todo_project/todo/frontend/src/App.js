import logo from './logo.svg';
import './App.css';
import React from 'react';
import UserList from './components/user.js';
import ProjectList from './components/projects.js';
import MenuList from './components/menu.js';
import NotFound404 from './components/not_found.js';
import FooterList from './components/footer.js';
import ProjectUserList from './components/project_user.js';
import TodoList from './components/todo.js';

import axios from 'axios';
import{HashRouter, Route, Switch, Link, Redirect} from 'react-router-dom';


class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': [],
            'projects': [],
            'project_user': {},
            'todos': []
        }
    }
    componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users/').then(response => {
        this.setState(
                {
                    'users': response.data
                }
            )
        }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
        this.setState(
                {
                    'projects': response.data
                }
            )
        }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/todos/').then(response => {
        this.setState(
                {
                    'todos': response.data
                }
            )
        }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <HashRouter>
                <nav>
                    <ul>
                        <li><Link to='/'>Authors</Link></li>
                        <li><Link to='/projects'>Projects</Link></li>
                        <li><Link to='/todos'>Todos</Link></li>
                    </ul>
                </nav>
                <MenuList />
                <Switch>
                    <Route exact path='/' component={() => <UserList users={this.state.users}/>} />
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>} />

                    <Route exact path='/todos' component={() => <TodoList todos={this.state.todos} />} />
                    <Route path='/projects/:id'><ProjectUserList projects={this.state.projects} />
                    </Route>
                    <Redirect from='/project' to='/projects' />
                    <Redirect from='/todo' to='/todos' />
                    <Route component={NotFound404}/>
                </Switch>
                <FooterList />
                </HashRouter>
            </div>
        )
    }
}

export default App;

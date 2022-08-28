import React from 'react'
import {Link, useParams} from "react-router-dom";



const ProjectItem = ({project}) => {
    return (
        <tr>
            <td> {project.url} </td>
            <td> <Link to={`/projects/${project.id} `}>{project.name}</Link> </td>
            <td> {project.repository} </td>
            <td> {project.users.name} </td>
        </tr>
    )
}


const ProjectUserList = ({notes}) => {
    let {id} = useParams();
    console.log(id)
    let filter_project = notes.filter((note => note.users.includes(parseInt(id))))
    return (
        <table>
             <tr>
                <th> Url </th>
                <th> Name </th>
                <th> Repository </th>
                <th> Users </th>
             </tr>
             {filter_project.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectUserList

import React from 'react'
import {Link} from "react-router-dom";

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

const ProjectList = ({projects}) => {
    return (
        <table>
            <tr>
                <th> Url </th>
                <th> Name </th>
                <th> Repository </th>
                <th> Users </th>
            </tr>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}


export default ProjectList

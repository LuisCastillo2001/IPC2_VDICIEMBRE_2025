
import {Routes, Route } from 'react-router-dom'


import NavBar from './components/NavBar'
import Home from './views/Home'
import Users from './views/Users'
import AddUser from './views/AddUser'


function App(){
  return (
    <div className='app-container'>
      <NavBar/>
      

      <main className = "content">
        <Routes>
          <Route path="/" element ={<Home/>} />
        </Routes>
        <Routes>
          <Route path='/usuarios' element={<Users/>}></Route>
        </Routes>
        <Routes>
        <Route path="/agregar" element={<AddUser />} />
        </Routes>
      </main>
      
    </div>
  )
}

export default App

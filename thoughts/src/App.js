import './App.css';
// import Home from './home/Home';

function App() {
  const isLoggedIn = false;
  const user = { name: "Username" };
  return (
    <div className="App">
      <nav>
        <p className='text-6x1 font-bold'>Welcome {isLoggedIn ? user.name : "to Thoughts"}</p>
      </nav>
      {/* <Home /> */}
    </div>
  );
}

export default App;

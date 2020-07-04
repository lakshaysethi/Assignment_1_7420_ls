import React, { useState, useEffect } from 'react'
import axios from 'axios';
const App = props => {
    useEffect(() => {
      axios.get('/api/profiles')
        .then(res => setState(res.data))
    }, [])
const [state, setState] = useState('')
return(
    <div>
      <p>{state.response_text}</p>
    </div>
 )
};
export default App;
import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import * as marked from 'marked';

export default class App extends React.Component{  
  constructor(props) {
    super(props);
    this.state = {
      markdown: '# Sample Markdown Heading\n\nEdit or replace this\n-----------\n\n### Another deeper heading\n\nParagraphs are separated by a blank line.\n\nLeave 2 spaces at the end of a line to do a  line break\n\nText attributes *italic*, **bold**,\n`monospace`, ~~strikethrough~~ .\n\nUnordered list:\n\n  * apples\n  * oranges\n  * pears\n\nNumbered list:\n\n  1. apples\n  2. oranges\n  3. pears\n\n---\n\n#### Created by:\n#### Foxy Nhi'
    }
  }
  updateMarkdown(markdown) {
    this.setState({markdown})
  }
  
  render() {
    const titleStyle = {
      display: 'flex',
      justifyContent: 'center',
      width: '100%', 
      height: '20vh',
      alignItems: 'center',
    }

    const boxStyle = {
      border: '1px solid black',
      width: 700,
      height: '60vh',
      padding: 0,
      margin: 0,
      boxSizing: 'content-box',
      backgroundColor: '#0b0a0a',
    }

    const inputStyle = {
      width: '100%',
      height: 'calc(60vh - 50px)',
      backgroundColor: '#222',
      color: 'white',
      padding: '0.5rem',
      resize: 'none',
      border: 'none',
    }

    const outputStyle = {
      width: '100%',
      height: 'calc(60vh - 50px)',
      padding: '0.5rem',
      overflow: 'auto',
      backgroundColor: '#ddd',
    }

    const headerStyle = {
      width: 700, 
      height: 50,
      borderBottom: '1px solid black',
      textAlign: 'center',
      paddingTop: 5,
      backgroundColor: '#a91c19',
      color: '#fff'
    }

    return (
      <div>
        <div style={titleStyle}>
          <h1 className='text-center'>Markdown Previewer</h1>
        </div>

        <div className='row'>
          <div className='col-6 mx-auto' style={boxStyle}>
            <div style={headerStyle}>
              <h2 className='text-center'>Editor</h2>
            </div>
            <textarea 
              className="input"
              style={inputStyle}
              value={this.state.markdown}
              onChange={(e) => {
                this.updateMarkdown(e.target.value);
              }}>                
              </textarea>
          </div>
          <div className='col-6 mx-auto' style={boxStyle}>
            <div style={headerStyle}>
              <h2 className='text-center'>Previewer</h2>
            </div>
            <div style={outputStyle}
              dangerouslySetInnerHTML={{ 
                __html: marked.parse(this.state.markdown) }}>
            </div>
          </div>
        </div>
      </div>   
    )            
  }
};

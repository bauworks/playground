import React from "react";

interface ISocketMessageState {
  endpoint: string;
  messages: Array<string>;
}

class SocketMessage extends React.Component {
  state: ISocketMessageState;

  constructor(props: any) {
    super(props);
    this.state = {
      endpoint: "ws://localhost:9999",
      messages: [],
    };
  }

  componentDidMount() {
    // initialize connection
    const ws = new WebSocket(this.state.endpoint);
    // ws.onopen = () =>{
    //  //send any msg from Client if needed
    //  ws.send(JSON.stringify(temp))
    // }
    // save whatever response from client
    ws.onmessage = (evt) => {
      this.setState({
        messages: this.state.messages.concat(evt.data),
      });
    };
  }

  componentWillUnmount() {
    this.setState({
      endpoint: "",
      messages: [],
    });
  }

  render() {
    return (
      <div>
        <p>
          {this.state.messages.map((items: React.ReactNode, index: number) => (
            <li key="index">
              {index} : {items}
            </li>
          ))}
        </p>
      </div>
    );
  }
}

export default SocketMessage;

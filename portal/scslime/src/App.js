import React, { useState } from "react";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";
import uuid from "uuid/v4";
import ContentEditable from "react-contenteditable";

const book0 = [];
const book1 = [];
const book2 = [
  // {id: uuid(), content: 'ikeem'}
];

const preKets = {
  [uuid()]: {
    name: "pre",
    items: book0
  }
};

const kets = {
  [uuid()]: {
    name: "  ", // invisible character
    items: book0
  },
  [uuid()]: {
    name: "ket 1",
    items: book1
  },
  [uuid()]: {
    name: "ket 2",
    items: book2
  }
};

const clusterKeys = Object.keys(kets);

const onDragEnd = (result, columns, setColumns) => {
  if (!result.destination) return;
  const { source, destination } = result;
  if (source.droppableId !== destination.droppableId) {
    const sourceColumn = columns[source.droppableId];
    const destColumn = columns[destination.droppableId];
    const sourceItems = [...sourceColumn.items];
    const destItems = [...destColumn.items];
    const [removed] = sourceItems.splice(source.index, 1);
    destItems.splice(destination.index, 0, removed);
    setColumns({
      ...columns,
      [source.droppableId]: {
        ...sourceColumn,
        items: sourceItems
      },
      [destination.droppableId]: {
        ...destColumn,
        items: destItems
      }
    });
  } else {
    const column = columns[source.droppableId];
    const copiedItems = [...column.items];
    const [removed] = copiedItems.splice(source.index, 1);
    copiedItems.splice(destination.index, 0, removed);
    setColumns({
      ...columns,
      [source.droppableId]: {
        ...column,
        items: copiedItems
      }
    });
  }
};

//////////////////////////////////////////////////////////////

function Console({ onAdd }) {
  const [value, setValue] = useState("   ");
  const onChange = ({ target: { value } }) => setValue(value);
  return (
    <div
      style={{
        transform: "translateX(81px) translateY(-144px)",
        height: "81px",
        position: "absolute",
        opacity: "45%"
      }}
    >
      <button
        onClick={onAdd(value)}
        style={{
          zIndex: "-0",
          color: "rgba(255, 0, 216, 0.9)",
          borderColor: "transparent",
          fontFamily: "Montez",
          borderRadius: "27px",
          fontSize: "60px",
          width: "81px",
          transform: "translateY(190px) translateX(9px)",
          background:
            "-webkit-radial-gradient(rgba(255, 0, 216, 0.19), rgba(168, 255, 0, 0.0))"
        }}
      >
        {" "}
        +{" "}
      </button>
      {/*<input style={{fontSize: '27px', fontFamily: 'Montez', borderColor: 'transparent', borderRadius: '9px', opacity:'45%',*/}
      {/*    height: '27px', width: '117px', background: 'linear-gradient(to right bottom, rgba(196, 181, 255, 1), rgba(132,47,0,0.27)',transform: 'translateY(261px) translateX(-203px)'*/}
      {/*}} value={value} onChange={onChange} placeholder="" />*/}
    </div>
  );
}

function App() {
  const [columns, setColumns] = useState(kets);
  const [isContentEditable, setIsContentEditable] = useState(false);

  const onAdd = value => () => {
    setColumns(columns => {
      const nC = { ...columns };
      const id = clusterKeys[0];
      const c = { ...columns[id] };
      const ci = [...c.items];
      ci.push({ id: uuid(), content: value });
      c.items = ci;
      nC[id] = c;
      return nC;
    });
  };

  const onKeyUp = (column, index) => evt => {
    if (typeof evt.target === undefined) return;
    let html = evt.target.innerHTML;
    setColumns(columns => {
      const nC = { ...columns };
      nC[column].items[index].content = html;
      return nC;
    });
  };
  return (
    <div style={{ position: "relative", top: "27px" }}>
      <Console onAdd={onAdd} />
      <div
        style={{
          display: "flex",
          height: "95%",
          position: "absolute",
          top: 5,
          left: 90,
          opacity: "27%"
        }}
      >
        <DragDropContext
          onDragEnd={result => onDragEnd(result, columns, setColumns)}
        >
          {Object.entries(columns).map(([id, column]) => {
            return (
              <div
                key={id}
                style={{
                  display: "flex",
                  flexDirection: "column",
                  alignItems: "center",
                  fontFamily: "Montez, sans-serif",
                  color: "#913aff",
                  fontSize: 27,
                  padding: 5,
                  borderRadius: "19px"
                }}
              >
                <h2 style={{ fontSize: 19 * 3, height: 45 }}>{column.name}</h2>
                <h2
                  style={{
                    fontSize: 19 * 3,
                    height: 45,
                    top: "9px",
                    position: "absolute",
                    opacity: "60%",
                    color: "#ffa0f9"
                  }}
                >
                  {column.name}
                </h2>
                <div style={{ margin: 2 }}>
                  <Droppable droppableId={id} key={id}>
                    {(provided, snapshot) => {
                      return (
                        <div
                          {...provided.droppableProps}
                          ref={provided.innerRef}
                          style={{
                            padding: 9,
                            width: 144,
                            minHeight: 9,
                            opacity: "95%",
                            borderRadius: "9px",
                            background:
                              "linear-gradient(to right bottom, rgba(196, 181, 255, 1), rgba(132,47,0,0.27)"
                          }}
                        >
                          {column.items.map((item, index) => {
                            return (
                              <Draggable
                                key={item.id}
                                draggableId={item.id}
                                index={index}
                              >
                                {(provided, snapshot) => {
                                  return (
                                    <div
                                      ref={provided.innerRef}
                                      {...provided.draggableProps}
                                      {...provided.dragHandleProps}
                                      style={{
                                        //opacity: "95%",
                                        padding: '9px',
                                        userSelect: "none",
                                        margin: "0px 0px 3px 0px",
                                        backgroundColor: snapshot.isDragging
                                          ? "#54ffff"
                                          : "#b3f542",
                                        background:
                                          "linear-gradient(to right bottom, rgba(84, 255, 255, 0.63), rgba(179, 245, 66, 0.81)",
                                        color: "rgb(75,29,0)",
                                        fontFamily: "Montez",
                                        fontWeight: 'bold',
                                        fontSize: 27,
                                        borderRadius: "9px",
                                        ...provided.draggableProps.style
                                      }}
                                    >
                                      <ContentEditable
                                        html={item.content}
                                        onKeyUp={onKeyUp(id, index)}
                                        onDoubleClick={() =>
                                          setIsContentEditable(
                                            !isContentEditable
                                          )
                                        }
                                        disabled={isContentEditable}
                                        style={{
                                          minHeight: 50,
                                          width: "100%"
                                        }}
                                      />
                                    </div>
                                  );
                                }}
                              </Draggable>
                            );
                          })}
                          {provided.placeholder}
                        </div>
                      );
                    }}
                  </Droppable>
                </div>
              </div>
            );
          })}
        </DragDropContext>
      </div>
    </div>
  );
}

export default App;

import React, { useState, useEffect } from 'react'
import {Tile} from '../Atoms/Tile';


//***********************************
// ブロックのパターン別色設定
//***********************************
const toColor = (code: number) : string => {
  switch (code) {
    case 1:   // The cube tile (block 2x2)
      return "grey";
    case 2:   // The I tile
      return "red";
    case 3:   // The T tile
      return "green";
    case 4:   // The inverse L tile
      return "blue";
    case 5:   // The L tile
      return "orange";
    case 6:   // The Z tile
      return "purple";
    case 7:   // The inverse Z tile
      return "maroon";
    default:  // Space
      return "white";
  };
};

//***********************************
// ブロックのパターン
//***********************************
const blockPatterns: number[][][][] = [
  [
    // The default square
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0]],
    [[0, 0], [0, 0], [0, 0], [0, 0]]
  ],
  [
    // The cube tile (block 2x2)
    [[0, 0], [1, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [0, 1], [1, 1]],
    [[0, 0], [1, 0], [0, 1], [1, 1]]
  ],
  [
    // The I tile
    [[0, -1], [0, 0], [0, 1], [0, 2]],
    [[-1, 0], [0, 0], [1, 0], [2, 0]],
    [[0, -1], [0, 0], [0, 1], [0, 2]],
    [[-1, 0], [0, 0], [1, 0], [2, 0]]
  ],
  [
    // The T tile
    [[0, 0], [-1, 0], [1, 0], [0, -1]],
    [[0, 0], [1, 0], [0, 1], [0, -1]],
    [[0, 0], [-1, 0], [1, 0], [0, 1]],
    [[0, 0], [-1, 0], [0, 1], [0, -1]]
  ],
  [
    // The inverse L tile
    [[0, 0], [-1, 0], [1, 0], [-1, -1]],
    [[0, 0], [0, 1], [0, -1], [1, -1]],
    [[0, 0], [1, 0], [-1, 0], [1, 1]],
    [[0, 0], [0, 1], [0, -1], [-1, 1]]
  ],
  [
    // The L tile
    [[0, 0], [1, 0], [-1, 0], [1, -1]],
    [[0, 0], [0, 1], [0, -1], [1, 1]],
    [[0, 0], [1, 0], [-1, 0], [-1, 1]],
    [[0, 0], [0, 1], [0, -1], [-1, -1]]
  ],
  [
    // The Z tile
    [[0, 0], [1, 0], [0, -1], [-1, -1]],
    [[0, 0], [1, 0], [0, 1], [1, -1]],
    [[0, 0], [1, 0], [0, -1], [-1, -1]],
    [[0, 0], [1, 0], [0, 1], [1, -1]]
  ],
  [
    // The inverse Z tile
    [[0, 0], [-1, 0], [0, -1], [1, -1]],
    [[0, 0], [0, -1], [1, 0], [1, 1]],
    [[0, 0], [-1, 0], [0, -1], [1, -1]],
    [[0, 0], [0, -1], [1, 0], [1, 1]]
  ]
]


//***********************************
// ブロックを指定座標にセットする関数
//***********************************
type putBlockProps = {
  x: number;
  y: number;
  block: number;
  rotate: number;
}
const putBlock = (props: putBlockProps,
                  bfProps: putBlockProps,
                  allTiles:　number[][]) :boolean => {
  const x: number = props.x;
  const y: number = props.y;
  const block: number = props.block;
  const rotate: number = props.rotate;

  const bf_x: number = bfProps.x;
  const bf_y: number = bfProps.y;
  const bf_block: number = bfProps.block;
  const bf_rotate: number = bfProps.rotate;

  console.log('putBlock()開始');
  console.log(bf_x + ", " + bf_y + ", " + bf_block + ", " + bf_rotate);
  console.log(x + ", " + y + ", " + block + ", " + rotate);

  if ( bf_x >= 0 ){
    console.log('前回セットしたブロックをクリアする');

    console.log('0:[' + (y + blockPatterns[block][rotate][0][0]) + '][' + (x + blockPatterns[block][rotate][0][1]) + ']');
    console.log('1:[' + (y + blockPatterns[block][rotate][1][0]) + '][' + (x + blockPatterns[block][rotate][1][1]) + ']');
    console.log('2:[' + (y + blockPatterns[block][rotate][2][0]) + '][' + (x + blockPatterns[block][rotate][2][1]) + ']');
    console.log('3:[' + (y + blockPatterns[block][rotate][3][0]) + '][' + (x + blockPatterns[block][rotate][3][1]) + ']');

    // 前回セットしたブロックをクリアする
    allTiles[ bf_y + blockPatterns[bf_block][bf_rotate][0][0] ][ bf_x + blockPatterns[bf_block][bf_rotate][0][1] ] = 0;
    allTiles[ bf_y + blockPatterns[bf_block][bf_rotate][1][0] ][ bf_x + blockPatterns[bf_block][bf_rotate][1][1] ] = 0;
    allTiles[ bf_y + blockPatterns[bf_block][bf_rotate][2][0] ][ bf_x + blockPatterns[bf_block][bf_rotate][2][1] ] = 0;
    allTiles[ bf_y + blockPatterns[bf_block][bf_rotate][3][0] ][ bf_x + blockPatterns[bf_block][bf_rotate][3][1] ] = 0;

    console.log('新しくブロックをセットして良いかチェックする');
    // 新しくブロックをセットして良いかチェックする
    if (
        y + blockPatterns[block][rotate][0][0] > allTiles.length -1 ||
        y + blockPatterns[block][rotate][1][0] > allTiles.length -1 ||
        y + blockPatterns[block][rotate][2][0] > allTiles.length -1 ||
        y + blockPatterns[block][rotate][3][0] > allTiles.length -1 ||
        x + blockPatterns[block][rotate][0][1] > allTiles[0].length -1 ||
        x + blockPatterns[block][rotate][1][1] > allTiles[0].length -1 ||
        x + blockPatterns[block][rotate][2][1] > allTiles[0].length -1 ||
        x + blockPatterns[block][rotate][3][1] > allTiles[0].length -1 ||
        allTiles[ y + blockPatterns[block][rotate][0][0] ][ x + blockPatterns[block][rotate][0][1] ] !== 0 ||
        allTiles[ y + blockPatterns[block][rotate][1][0] ][ x + blockPatterns[block][rotate][1][1] ] !== 0 ||
        allTiles[ y + blockPatterns[block][rotate][2][0] ][ x + blockPatterns[block][rotate][2][1] ] !== 0 ||
        allTiles[ y + blockPatterns[block][rotate][3][0] ][ x + blockPatterns[block][rotate][3][1] ] !== 0 ){

          console.log('チェックNG => 前回セットしたブロックを元に戻す');
          // 前回セットしたブロックを元に戻す
          allTiles[ bf_y + blockPatterns[bf_block][bf_rotate][0][0] ][ bf_x + blockPatterns[bf_block][bf_rotate][0][1] ] = bf_block;
          allTiles[ bf_y + blockPatterns[bf_block][bf_rotate][1][0] ][ bf_x + blockPatterns[bf_block][bf_rotate][1][1] ] = bf_block;
          allTiles[ bf_y + blockPatterns[bf_block][bf_rotate][2][0] ][ bf_x + blockPatterns[bf_block][bf_rotate][2][1] ] = bf_block;
          allTiles[ bf_y + blockPatterns[bf_block][bf_rotate][3][0] ][ bf_x + blockPatterns[bf_block][bf_rotate][3][1] ] = bf_block;
          return false;
    }
  }

  console.log('新しくブロックをセットする');
  // 新しくブロックをセットする
  allTiles[ y + blockPatterns[block][rotate][0][0] ][ x + blockPatterns[block][rotate][0][1] ] = block;
  allTiles[ y + blockPatterns[block][rotate][1][0] ][ x + blockPatterns[block][rotate][1][1] ] = block;
  allTiles[ y + blockPatterns[block][rotate][2][0] ][ x + blockPatterns[block][rotate][2][1] ] = block;
  allTiles[ y + blockPatterns[block][rotate][3][0] ][ x + blockPatterns[block][rotate][3][1] ] = block;

  return true;
}


//***********************************
// タイルボード コンポーネント
//***********************************
type Props = {
  width: number;
  height: number;
}
export const TilesBoard: React.FC<Props> = (props: Props) => {

    //-------------------------------
    // ステータス
    //-------------------------------
    /*
     * 全タイル情報
     */

    const initialTilesInfo = () => {
      console.log('initialTilesInfo() Start');
      const infos: number[][] = new Array<number[]>(props.height);
      for (let i=0; i < infos.length; i++){
        infos[i] = new Array<number>(props.width).fill(0);
      }
      return infos;
    } 
    const [tilesInfo, setTilesInfo] = useState<number[][]>(initialTilesInfo);


    /*
     * 前回のタイル更新Props
     */
    const [bfProps, setBfProps] = useState<putBlockProps>({x:-1, y:-1, block:-1, rotate:-1});


    /*
     * 移動後のブロック位置
     */
    const [nextPos, setNextPos] = useState<number[]>([6, 2]);


    //-------------------------------
    // タイルを並べる(列)
    //-------------------------------
    const tilesRow = (rowInfo: number[]) => (rowInfo.map((info) => 
      <Tile bgcolor={toColor(info)} />
    ));

    //-------------------------------
    // タイルを並べる(行)
    //-------------------------------
    const tilesAll = tilesInfo.map((rowInfo, index) => 
      <div>
        {tilesRow(rowInfo)}
      </div>
    );



    //-------------------------------
    // ブロック移動指示
    //-------------------------------
    // ブロックを下に落とす
    const downBlock = () => {
      setNextPos(xy => [xy[0], xy[1]+1]);
    };

    useEffect(() => {
      // Props編集
      const props :putBlockProps = {
        x: nextPos[0],
        y: nextPos[1],
        block: Math.floor( Math.random() * (6+1) )+1,
        rotate: Math.floor( Math.random() * (3+1) )
      }
      // ブロックをセットする
console.log('ブロックをセットする]');
      const ret = putBlock(props, bfProps, tilesInfo);

      if (ret === true) {
        // ブロックの移動が成功の場合は、Propsを前回値として保存
        setBfProps(props);
      } else {
        // ブロックの移動が失敗の場合は、nextPosを前回値に戻す
        setNextPos([bfProps.x, bfProps.y]);
      }

      // タイル情報を更新
      setTilesInfo(tilesInfo);

    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [nextPos]);
  
    // タイマー処理（ブロック降下）
    useEffect(() => {
      const timerId = setInterval(downBlock, 1000);
      return () => clearInterval(timerId);
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);


    //------------------------
    // スタイル設定
    //------------------------
    // タイルボード
    const tileBoardStyle: React.CSSProperties = {
      width: "400px",
      height: "400px",
      display: "table"
    };

    //-------------------------------
    // JSX
    //-------------------------------  
    return (
      <div style={tileBoardStyle}>
        {tilesAll}
      </div>
    )
}
  
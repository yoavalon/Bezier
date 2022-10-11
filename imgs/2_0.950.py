d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)

d.end()

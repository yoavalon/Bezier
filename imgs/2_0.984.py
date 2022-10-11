d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NW, Length.long)
d.position_pen(2,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()

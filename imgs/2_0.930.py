d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,3)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)

d.end()

d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.long)

d.end()

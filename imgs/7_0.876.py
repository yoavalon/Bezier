d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.low)
d.position_pen(1,1)

d.end()

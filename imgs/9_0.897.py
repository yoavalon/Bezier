d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.SW, Length.long)
d.position_pen(3,2)
d.straight_line(Direction.SE, Length.long)
d.position_pen(0,1)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)

d.end()

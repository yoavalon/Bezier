d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(3,1)
d.straight_line(Direction.W, Length.long)

d.end()

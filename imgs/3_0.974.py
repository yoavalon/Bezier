d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()

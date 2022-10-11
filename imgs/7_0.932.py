d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)

d.end()

d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)

d.end()

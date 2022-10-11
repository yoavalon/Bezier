d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(0,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)

d.end()

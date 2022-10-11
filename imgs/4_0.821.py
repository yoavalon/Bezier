d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,2)

d.end()

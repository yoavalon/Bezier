d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.position_pen(0,2)

d.end()

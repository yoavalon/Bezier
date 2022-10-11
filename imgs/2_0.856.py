d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.short)
d.position_pen(1,0)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()

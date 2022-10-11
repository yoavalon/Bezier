d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.NW, Length.long)

d.end()

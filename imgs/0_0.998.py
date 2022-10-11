d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)
d.position_pen(3,0)

d.end()
